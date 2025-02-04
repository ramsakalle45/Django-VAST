# myapp\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_item, name='create_item'),
    path('list/', views.item_list, name='item_list'),
    path('api/items/', views.item_list_api, name='item_list_api'),
    path('api/items/<int:pk>/', views.item_detail_api, name='item_detail_api'),
    path('contact', views.contact, name='contact')
    
]