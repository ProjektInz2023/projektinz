
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include

urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]
