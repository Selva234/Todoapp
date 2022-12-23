from django.db import models

##create your models here.
class Todo(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=200)
