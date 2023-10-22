from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from api.models import Staff, MainCourse, Order

class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = Staff
        fields = ["email", "name", "surname"]

    def clean_password2(self):
        
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Staff
        fields = ["email", "password", "name", "surname", "created", "is_active", "is_admin"]

class UserAdmin(BaseUserAdmin):
    
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["email", "name", "surname", "created", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name", "surname", "created"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name", "surname", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []

class MainCourseAdmin(admin.ModelAdmin):
    list_display = ["mainCourseId", "name", "description", "price"]
    ordering = ["mainCourseId"]

class OrderAdmin(admin.ModelAdmin):
    list_display = ["orderId", "user", "mainCourse", "date", "status"]
    ordering = ["-date"]
    list_filter = ["status"]

admin.site.register(Staff, UserAdmin)
admin.site.register(MainCourse, MainCourseAdmin)
admin.site.register(Order, OrderAdmin)