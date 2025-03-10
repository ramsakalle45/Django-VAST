# myapp\views.py
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import ContactForm, ItemForm, PostForm, AuthorForm, BookForm
from .models import Item, Post, Book
from .serializers import ItemSerializer, PostSerializer
from flask import request

# Home Page View
def home(request):
    context = {'message': 'Welcome to the Home Page!'}
    return render(request, 'myapp/home.html', context)

# Contact Form View
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'myapp/contact.html', {'form': form})

# Create Item (HTML Form)
def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'myapp/item_form.html', {'form': form})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'myapp/create_post.html', {'form': form})
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'myapp/post_list.html', {'posts': posts})        

# Item List (HTML)
def item_list(request):
    items = Item.objects.all()
    return render(request, 'myapp/item_list.html', {'items': items})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'myapp/book_form.html', {'form': form})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = AuthorForm()
    return render(request, 'myapp/author_form.html', {'form': form})





#################API Part#######################

# ✅ API View for Item List (GET & POST)
@api_view(['GET', 'POST'])
def item_list_api(request):
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Debugging: Print request content type and data
        print("Content-Type:", request.content_type)
        print("Received Data:", request.data)

        # Check if data exists
        if not request.data:
            return Response({"error": "Empty request body. Make sure to send JSON data."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ API View for Single Item (GET, PUT, DELETE)
@api_view(['GET', 'PUT', 'DELETE'])
def item_detail_api(request, pk):
    try:
        item = Item.objects.get(pk=pk)
        
    except Item.DoesNotExist:
        return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        print("Received Data:", request.data)  # Debugging - Check in Django console
        if not request.data:
            return Response({"error": "No data received"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response({"message": "Item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def post_list_api(request):
    if request.method == 'GET':
        items = Post.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Debugging: Print request content type and data
        print("Content-Type:", request.content_type)
        print("Received Data:", request.data)

        # Check if data exists
        if not request.data:
            return Response({"error": "Empty request body. Make sure to send JSON data."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'POST'])
def post_list_api(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Debugging: Print request content type and data
        print("Content-Type:", request.content_type)
        print("Received Data:", request.data)

        # Check if data exists
        if not request.data:
            return Response({"error": "Empty request body. Make sure to send JSON data."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def post_detail_api(request, pk):
    try:
        posts = Post.objects.get(pk=pk)
        
    except Item.DoesNotExist:
        return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(posts)
        return Response(serializer.data)

    elif request.method == 'PUT':
        print("Received Data:", request.data)  # Debugging - Check in Django console
        if not request.data:
            return Response({"error": "No data received"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PostSerializer(posts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        posts.delete()
        return Response({"message": "Item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

from .models import Book, Author 
from .serializers import BookSerializer, AuthorSerializer

@api_view(['GET', 'POST'])
def book_list_api(request):
    if request.method == 'GET':
        items = Book.objects.all()
        serializer = BookSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Debugging: Print request content type and data
        print("Content-Type:", request.content_type)
        print("Received Data:", request.data)

        # Check if data exists
        if not request.data:
            return Response({"error": "Empty request body. Make sure to send JSON data."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def book_detail_api(request, pk):
    try:
        posts = Book.objects.get(pk=pk)
        
    except Book.DoesNotExist:
        return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(posts)
        return Response(serializer.data)

    elif request.method == 'PUT':
        print("Received Data:", request.data)  # Debugging - Check in Django console
        if not request.data:
            return Response({"error": "No data received"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = BookSerializer(posts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        posts.delete()
        return Response({"message": "Item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# Single API for Author
@api_view(['GET', 'POST'])
def author_list_api(request):
    if request.method == 'GET':
        items = Author.objects.all()
        serializer = AuthorSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Debugging: Print request content type and data
        print("Content-Type:", request.content_type)
        print("Received Data:", request.data)

        # Check if data exists
        if not request.data:
            return Response({"error": "Empty request body. Make sure to send JSON data."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
 
 #API for operating with the primary key
@api_view(['GET', 'PUT', 'DELETE'])
def author_detail_api(request, pk):
    try:
        posts = Author.objects.get(pk=pk)
        
    except Author.DoesNotExist:
        return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AuthorSerializer(posts)
        return Response(serializer.data)

    elif request.method == 'PUT':
        print("Received Data:", request.data)  # Debugging - Check in Django console
        if not request.data:
            return Response({"error": "No data received"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = AuthorSerializer(posts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        posts.delete()
        return Response({"message": "Item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)    