from django.shortcuts import render
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Order
from .serializers import OrderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  permissions

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['name'] = user.name
        token['surname'] = user.surname

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
  
class OrderView(APIView):
    #permission_classes = [permissions.IsAuthenticated]
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        orders = Order.objects.filter()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)