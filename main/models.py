import uuid
from django.db import models

class Products(models.Model):
    CATEGORY_CHOICES = [
        ('sepatu', 'Sepatu'),
        ('bola', 'Bola'),
        ('jersey', 'Jersey'),
        ('celana', 'Celana'),
        ('baju', 'Baju'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    thumbnail = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
