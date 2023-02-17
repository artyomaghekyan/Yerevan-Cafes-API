from django.db import models
from django.utils import timezone

# Create your models here.

class Cafes(models.Model):
    name = models.CharField(max_length=200)
    rating = models.FloatField(default=1.1)
    location = models.CharField(max_length=200)
    created = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ['-created']


    def __str__(self) -> str:
        return self.name
