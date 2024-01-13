from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import MainCourse, Order, Staff
from rest_framework import status
from .serializers import CreateUserSerializer, MainCourseSerializer, Order2Serializer, OrderSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from django.views import View
import stripe
from django.conf import settings
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckoutSessionView(View):
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        
        YOUR_DOMAIN = "http://127.0.0.1:8000"

        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': 'price_1OVz6kA8AWLRKBxKnJhc2r5f',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '?success=true',
            cancel_url=YOUR_DOMAIN + '?canceled=true',
        )
        return JsonResponse({
            'id': checkout_session.id
        })



#class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
 #   @classmethod
  #  def get_token(cls, user):
   #     token = super().get_token(user)
#
 #       token['name'] = user.name
  #      token['surname'] = user.surname
#
 #       return token

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        data['name'] = self.user.name
        data['surname'] = self.user.surname

    
        data['user'] = {
            'id': self.user.id,
            'email': self.user.email,
            'name': self.user.name,
            'surname': self.user.surname,
            'role': {
                'id': self.user.role.id,
                'name': self.user.role.name
            }
        }

        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class CookLoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            user_data = response.data.get('user', {})
            role_name = user_data.get('role', {}).get('name')
            if role_name and role_name != 'Cook':
                return Response({"detail": "Invalid credentials"}, status=403)
        return response

class AdminLoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            # Extract user information from the response data
            user_data = response.data.get('user', {})
            role_name = user_data.get('role', {}).get('name')
            if role_name and role_name != 'Manager':
                return Response({"detail": "Invalid credentials"}, status=403)
        return response
    
@api_view(['GET'])
def all_orders(request):
    # checking for the parameters from the URL
    if request.query_params:
        orders = Order.objects.filter(**request.query_params.dict())
    else:
        orders = Order.objects.all()
 
    # if there is something in items else raise error
    if orders:
        serializer = Order2Serializer(orders, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def update_order(request, pk):
    order = Order.objects.get(pk=pk)
    data = OrderSerializer(instance=order, data=request.data)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PATCH'])
def patch_order(request, pk):
    order = Order.objects.get(pk=pk)
    data = OrderSerializer(instance=order, data=request.data, partial=True)
 
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def delete_order(request, pk):
    item = get_object_or_404(Order, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

class MainCourseList(APIView):
    def get(self, request, *args, **kwargs):
        main_courses = MainCourse.objects.all()
        serializer = MainCourseSerializer(main_courses, many=True)
        return Response(serializer.data)
    

class MainCourseListCreateView(generics.ListCreateAPIView):
    queryset = MainCourse.objects.all()
    serializer_class = MainCourseSerializer

    def post(self, request, *args, **kwargs):
        serializer = MainCourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MainCourseRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = MainCourse.objects.all()
    serializer_class = MainCourseSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = MainCourseSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MainCourseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MainCourse.objects.all()
    serializer_class = MainCourseSerializer

    
class UserOrders(APIView):
    def get(self, request, email, *args, **kwargs):
        orders = Order.objects.filter(user__email=email)
        serializer = Order2Serializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def add_order(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def create_user(request):
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_by_email(request, email):
    try:
        user = Staff.objects.get(email=email)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=200)
    except Staff.DoesNotExist:
        return Response({"detail": "User not found"}, status=404)
    
@api_view(['GET'])
def get_all_users(request):
    users = Staff.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=200)

@api_view(['PUT', 'DELETE'])
def update_or_delete_user(request, email):
    user = get_object_or_404(Staff, email=email)

    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return Response({"detail": "User deleted successfully"}, status=204)