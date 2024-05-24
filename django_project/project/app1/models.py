from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class Mobile(models.Model):
    mobile = models.IntegerField()
    uid = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
    
class Todo(models.Model):
    todo_items = models.CharField(max_length=50)
    status = models.CharField(default='Not started', max_length=50)
    due = models.DateField(auto_now=False, auto_now_add=False)
    uid = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    