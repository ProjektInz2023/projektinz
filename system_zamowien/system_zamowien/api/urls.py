from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import MyTokenObtainPairView, OrderView



urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('orders/', OrderView.as_view(), name='orders'),
]