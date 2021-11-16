from rest_framework import status
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet 
from .serializers import  PostSerializer 
from .models import Post
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()     
    serializer_class = PostSerializer

