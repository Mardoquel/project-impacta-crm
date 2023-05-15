from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('add_record/', views.add_record, name='add_record'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
]
