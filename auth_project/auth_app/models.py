from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class BlogModel(models.Model):
    username= models.CharField(max_length=300)
    foreignkey= models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    blogtitle = models.CharField(max_length= 300)
    blogentry = models.CharField(max_length=300)
    createDate= models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.username