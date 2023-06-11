from rest_framework import serializers
from .models import Order, MainCourse



class OrderSerializer(serializers.ModelSerializer):
    mainCourse = serializers.SlugRelatedField(
        read_only = True,
        slug_field = "name"
    )
    class Meta:
        model = Order      
        fields = ('user', 'mainCourse', 'date', 'status')