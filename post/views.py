from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Post
from .serializers import PostSerializer, Post_editSerializer
from rest_framework import generics
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated  

# Create your views here.
## Post

class List(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

class Write(CreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class Edit(generics.RetrieveUpdateAPIView):
    # permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    queryset = Post.objects.all()
    serializer_class = Post_editSerializer


class Delete(DestroyAPIView):
    # permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

class View(RetrieveAPIView):
    lookup_field = 'pk'
    queryset = Post.objects.all()
    serializer_class = PostSerializer