from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

user = get_user_model()


class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(user, on_delete=models.CASCADE)
    Created_date = models.DateTimeField(auto_now_add=True)
    Published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
