from django.db import models

# Create your models here.
class PhotoModel(models.Model):
    photo=models.FileField()
    file_name=models.TextField()
    file_description=models.TextField()
    file_date=models.DateTimeField(auto_now_add=True)