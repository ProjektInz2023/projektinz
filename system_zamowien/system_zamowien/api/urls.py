from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import MyTokenObtainPairView



urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('', views.ApiOverview, name='api-home'),
    path('orders/', views.all_orders, name='orders'),
    path('orders/<int:pk>/', views.update_order, name='update-order'),
    path('orders/<int:pk>/delete', views.delete_order, name='delete-order'),
    path('orders/patch/<int:pk>/', views.patch_order, name='patch-order'),
]