from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('about/',views.About, name='about'),
    path('contact/',views.Contact, name='contact'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('view_doctor/', views.View_doctor, name='view_doctor'),
    path('delete_doctor/<int:pid>/', views.Delete_doctor, name='delete_doctor'),

]