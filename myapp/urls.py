# myapp\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_item, name='create_item'),
    path('create-post', views.create_post, name='create_post'),
    path('post-list', views.post_list, name='post_list'),
    path('list/', views.item_list, name='item_list'),
    path('api/items/', views.item_list_api, name='item_list_api'),
    path('api/items/<int:pk>/', views.item_detail_api, name='item_detail_api'),
    path('api/posts/', views.post_list_api, name='post_list_api'),
    path('api/posts/<int:pk>/', views.post_detail_api, name='post_detail_api'),
    path('contact', views.contact, name='contact')
    
]