from django.db import models

# Create your models here.
class Users (models.Model):

    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):

        return self.id

class Post(models.Model):
   
    api_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.title