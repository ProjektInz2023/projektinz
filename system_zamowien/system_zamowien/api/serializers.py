from rest_framework import serializers
from .models import Alergen, Order, MainCourse, Staff



class OrderSerializer(serializers.ModelSerializer):
    #mainCourse = serializers.SlugRelatedField(
    #    slug_field = "name", queryset=MainCourse.objects.all()
    #)
    #mainCourse = serializers.PrimaryKeyRelatedField(queryset=MainCourse.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=Staff.objects.all())
    class Meta:
        model = Order
        fields = '__all__' 

class AlergenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alergen
        fields = '__all__'

class MainCourseSerializer(serializers.ModelSerializer):
    alergens = serializers.StringRelatedField(many=True)

    class Meta:
        model = MainCourse
        fields = '__all__'