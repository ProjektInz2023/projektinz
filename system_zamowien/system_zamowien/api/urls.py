from django.urls import path
from .views import LoginView, OrderView


urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('orders/', OrderView.as_view()),
]