from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import BlogPost
from .serializers import BlogSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer
