from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()  # Display author's username

    class Meta:
        model = Blog
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']