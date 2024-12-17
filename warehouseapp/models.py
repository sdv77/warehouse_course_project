from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
    

class TypeStorage(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Cell(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cells')

    def __str__(self):
        return f"Cell of {self.user.email}"

class CellItem(models.Model):
    cell = models.ForeignKey(Cell, on_delete=models.CASCADE, related_name='cell_items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item.name} in {self.cell}"

class ItemInfo(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, related_name='info')
    type_storage = models.ForeignKey(TypeStorage, on_delete=models.CASCADE, related_name='item_infos', null=True)
    description = models.TextField(null=True, blank=True)
    count = models.IntegerField(default=1)
    weight = models.IntegerField(default=1)

    def __str__(self):
        return f"Info for {self.item.name}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    description = models.TextField()
    
    def __str__(self):
        return f"Review by {self.user.email}"