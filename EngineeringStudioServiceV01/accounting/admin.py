# python manage.py runserver 192.168.0.214:8000
from django.contrib import admin
from django import forms
from django.forms import *
from django.forms import inlineformset_factory, BaseInlineFormSet
from django.forms import ModelForm
from .models import *
# from widgets import ImproveRawIdFieldsForm
from django.contrib.admin.options import StackedInline, TabularInline
from django_json_widget.widgets import JSONEditorWidget


@admin.register(WarehouseActionType)
class WarehouseActionTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(WarehouseFlow)
class WarehouseFlowAdmin(admin.ModelAdmin):
    list_display = ('action_type', 'creation_date')

@admin.register(ItemPlaceQuantity)
class ItemPlaceQuantityAdmin(admin.ModelAdmin):
    list_display = ('item', 'place','quantity', 'owner')

@admin.register(GeneralItem)
class GeneralItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('object_id', 'table_name', 'id',)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'parent', 'id',)


@admin.register(ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)


@admin.register(StandardCode)
class StandardCodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'description',)


@admin.register(Standard)
class StandardAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'description',)


@admin.register(ItemMaterial)
class ItemMaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'short_name', 'description',)


@admin.register(FastenerSize)
class FastenerSizeAdmin(admin.ModelAdmin):
    list_display = ('size', 'id',)


@admin.register(Bolt)
class BoltAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)


@admin.register(Nut)
class BoltAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)


@admin.register(GradeClass)
class GradeClassAdmin(admin.ModelAdmin):
    list_display = ('grade', 'id',)


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)



# class OrderNutInline(StackedInline):
#     model = OrderNut
#     extra = 0
#
#
# class OrderBoltInline(StackedInline):
#     model = OrderBolt
#     extra = 0
#
#
# class OrderAdmin(admin.ModelAdmin):
#     inlines = [
#         OrderNutInline,
#         OrderBoltInline,
#     ]
#
#     formfield_overrides = {
#         models.ForeignKey: {"widget": RadioSelect(choices=OrderStatus.objects.all())},
#     }


# admin.site.register(Order, OrderAdmin)

# class ItemPlaceQuantityInline(admin.TabularInline):
#     model = ItemPlaceQuantity
#     # extra = 0
#
#
#
# class WarehouseFlowAdmin(admin.ModelAdmin):
#     inlines = [
#         ItemPlaceQuantityInline,
#     ]
#
# admin.register(WarehouseFlow, WarehouseFlowAdmin)