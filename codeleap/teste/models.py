from django.db import models

# Create your models here.
class DataStructure(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    username = models.CharField(max_length=255)
    created_datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
