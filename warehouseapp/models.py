from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

class TypeStorage(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Item(models.Model):
    name = models.CharField(max_length=255)

class Role(models.Model):
    name = models.CharField(max_length=255)

class Cell(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cells')

class CellItem(models.Model):
    cell = models.ForeignKey(Cell, on_delete=models.CASCADE, related_name='cell_items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

class ItemInfo(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, related_name='info')
    description = models.TextField(null=True, blank=True)
    count = models.IntegerField(default=1)
    weight = models.IntegerField(default=1)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    description = models.TextField()