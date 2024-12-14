from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.
from .models import User, TypeStorage, Item, Role, Cell, CellItem, ItemInfo, Review

class UserResource(resources.ModelResource):
    class Meta:
        model = User

@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource
    list_display = ('id', 'name', 'email')
    search_fields = ('name', 'email')
    list_filter = ('email',)
    ordering = ('id',)

# Повтори аналогичные шаги для остальных моделей

class TypeStorageResource(resources.ModelResource):
    class Meta:
        model = TypeStorage

@admin.register(TypeStorage)
class TypeStorageAdmin(ImportExportModelAdmin):
    resource_class = TypeStorageResource
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('id',)

class ItemResource(resources.ModelResource):
    class Meta:
        model = Item

@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):
    resource_class = ItemResource
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('id',)

class RoleResource(resources.ModelResource):
    class Meta:
        model = Role

@admin.register(Role)
class RoleAdmin(ImportExportModelAdmin):
    resource_class = RoleResource
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('id',)

class CellResource(resources.ModelResource):
    class Meta:
        model = Cell

@admin.register(Cell)
class CellAdmin(ImportExportModelAdmin):
    resource_class = CellResource
    list_display = ('id', 'user')
    search_fields = ('user__name',)
    list_filter = ('user',)
    ordering = ('id',)

class CellItemResource(resources.ModelResource):
    class Meta:
        model = CellItem

@admin.register(CellItem)
class CellItemAdmin(ImportExportModelAdmin):
    resource_class = CellItemResource
    list_display = ('id', 'cell', 'item')
    search_fields = ('cell__id', 'item__name')
    list_filter = ('cell', 'item')
    ordering = ('id',)

class ItemInfoResource(resources.ModelResource):
    class Meta:
        model = ItemInfo

@admin.register(ItemInfo)
class ItemInfoAdmin(ImportExportModelAdmin):
    resource_class = ItemInfoResource
    list_display = ('id', 'item', 'description', 'count', 'weight')
    search_fields = ('item__name', 'description')
    ordering = ('id',)

class ReviewResource(resources.ModelResource):
    class Meta:
        model = Review

@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin):
    resource_class = ReviewResource
    list_display = ('id', 'user', 'description')
    search_fields = ('user__name', 'description')
    list_filter = ('user',)
    ordering = ('id',)