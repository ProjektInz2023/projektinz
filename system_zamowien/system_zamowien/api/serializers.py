from rest_framework import serializers
from .models import Alergen, Order, MainCourse, Staff
from django.contrib.auth.models import Group




class AlergenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alergen
        fields = ['name' ]

class MainCourseSerializer(serializers.ModelSerializer):
    alergens = AlergenSerializer(many=True)

    class Meta:
        model = MainCourse
        fields = '__all__'

    def create(self, validated_data):
        alergens_data = validated_data.pop('alergens', [])
        main_course = MainCourse.objects.create(**validated_data)

        for alergen_data in alergens_data:
            alergen, created = Alergen.objects.get_or_create(**alergen_data)
            main_course.alergens.add(alergen)

        return main_course
    
    def update(self, instance, validated_data):
        alergens_data = validated_data.pop('alergens', [])

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.image = validated_data.get('image', instance.image)

        instance.alergens.clear()  # Remove existing alergens
        for alergen_data in alergens_data:
            alergen, created = Alergen.objects.get_or_create(**alergen_data)
            instance.alergens.add(alergen)

        instance.save()
        return instance
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ('id', 'email', 'name', 'surname', 'role')

class OrderSerializer(serializers.ModelSerializer):
    #user = serializers.PrimaryKeyRelatedField(queryset=Staff.objects.all())
    #class Meta:
     #   model = Order
      #  fields = '__all__' 
    user = UserSerializer()
    mainCourse = MainCourseSerializer()
    class Meta:
        model = Order
        fields = '__all__'



class CreateUserSerializer(serializers.ModelSerializer):
    role_name = serializers.CharField(write_only=True)

    class Meta:
        model = Staff
        fields = ('email', 'name', 'surname', 'password', 'role_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        role_name = validated_data.pop('role_name', None)
        user = Staff.objects.create_user(**validated_data)

        if role_name:
            role, _ = Group.objects.get_or_create(name=role_name)
            user.role = role
            user.save()

        return user