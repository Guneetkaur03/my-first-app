from django.db import models
from django.utils import timezone
# Create your models here.

class note(models.Model):
    title = models.CharField(max_length = 50)
    subject = models.CharField(max_length=100)
    subject_teacher = models.CharField(max_length=20)
    file_type = models.CharField(max_length=5)
    uploaded_date = models.DateTimeField(default =timezone.now)
    
