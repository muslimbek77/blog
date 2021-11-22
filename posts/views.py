from typing import Generator, Generic
from django.shortcuts import render
from .permissions import IsAutorOrReadOnly
from .models import Post
from rest_framework import generics
from .serializers import PostSerializer

# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAutorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
