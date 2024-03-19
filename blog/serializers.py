from rest_framework import serializers
from .models import BlogPost

class BlogSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'text', 'image', 'author_name']