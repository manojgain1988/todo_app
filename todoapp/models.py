from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    user=models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    text =models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering= ('-created_at',)

    def __str__(self):
        return self.text
    