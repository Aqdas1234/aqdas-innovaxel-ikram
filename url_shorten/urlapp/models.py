from django.db import models
import string
import random

def generate_shortcode(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

class ShortURL(models.Model):
    url = models.URLField()
    shortCode = models.CharField(max_length=10, unique=True)
    accessCount = models.PositiveIntegerField(default=0)  
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.shortCode} -> {self.url}"
