from . import views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import AdminLoginView, CookLoginView, MainCourseList, MainCourseListCreateView, MainCourseRetrieveUpdateDestroyView, MainCourseRetrieveUpdateView, MyTokenObtainPairView, UserOrders, add_order, create_user, get_all_users, get_user_by_email, update_or_delete_user



urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logincook/', CookLoginView.as_view(), name='cook_login'),
    path('loginadmin/', AdminLoginView.as_view(), name='admin_login'),
    
    path('addstaff/', create_user, name='create_user'),
    path('staff/<str:email>/', get_user_by_email, name='get_user_by_email'),
    path('staff/', get_all_users, name='get_all_users'),
    path('edit_staff/<str:email>/', update_or_delete_user, name='update_or_delete_user'),
    path('delete_staff/<str:email>/', update_or_delete_user, name='update_or_delete_user'),
    
    path('orders/', views.all_orders, name='orders'),
    path('orders/<int:pk>/', views.update_order, name='update-order'),
    path('orders/<int:pk>/delete', views.delete_order, name='delete-order'),
    path('orders/patch/<int:pk>/', views.patch_order, name='patch-order'),
    path('orders/<str:email>/', UserOrders.as_view(), name='user-orders'),
    path('addorder/', add_order, name='order-api'),

    path('maincourses/', MainCourseList.as_view(), name='maincourse-list'),
    path('addmaincourse/', MainCourseListCreateView.as_view(), name='main_course-list-create'),
    path('maincourses/<int:pk>/', MainCourseRetrieveUpdateView.as_view(), name='main_course-retrieve-update'),
    path('deletemaincourse/<int:pk>/', MainCourseRetrieveUpdateDestroyView.as_view(), name='main_course-retrieve-update'),
]