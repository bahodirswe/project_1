from rest_framework import serializers
from .models import Category, Post, Comment, Trend
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'all'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'all'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = 'all'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = 'all'

class TrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trend
        fields = 'all'