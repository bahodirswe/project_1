from django.db import models
from user.models import User

class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self) -> str:
        return f"{self.name}"

#  CASCADE -----> Category (Technology) <---> Post(Yangilik 1) post ham o'chib ketadi.
#  SET_NULL -----> Category (Technology) <---> Post(Yangilik 1) post categorysi bo'sh bo'ladi.
    
#  class MyPostManager():
#      pass

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name ="post_category")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name ="post_author")
    name = models.CharField(max_length=150)
    summary = models.CharField(max_length=300)
    text = models.TextField()
    status = models.BooleanField(default=False)
    img = models.ImageField(upload_to="images/", blank=True)
    video = models.FileField(upload_to="videos/", blank=True)
    audio = models.FileField(upload_to="audios/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.category} - {self.name}"
    

    class Meta:
        ordering =('-created_at',)