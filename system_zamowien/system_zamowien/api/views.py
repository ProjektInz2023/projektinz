from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import MainCourse, Order, Staff
from rest_framework import status
from .serializers import MainCourseSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['name'] = user.name
        token['surname'] = user.surname

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def all_orders(request):
    # checking for the parameters from the URL
    if request.query_params:
        orders = Order.objects.filter(**request.query_params.dict())
    else:
        orders = Order.objects.all()
 
    # if there is something in items else raise error
    if orders:
        serializer = OrderSerializer(orders, many=True)
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
    
class UserOrders(APIView):
    def get(self, request, email, *args, **kwargs):
        orders = Order.objects.filter(user__email=email)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def add_order(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)