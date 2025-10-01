import uuid
from django.db import models
from django.contrib.auth.models import User

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
    item_sales = models.PositiveBigIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name

    @property
    def is_product_hot(self):
        return self.item_sales > 10
        
    def increment_sales(self):
        self.item_sales += 1
        self.save()
        
    def title(self):
        return self.name
    
    def content(self):
        return self.description
    
