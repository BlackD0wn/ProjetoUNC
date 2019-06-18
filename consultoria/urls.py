from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('deploy/', views.deploy, name='deploy'),
    path('post/list/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),

    path('accounts/registration/', views.registration, name='registration'),
]
