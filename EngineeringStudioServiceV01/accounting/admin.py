# python manage.py runserver 192.168.0.214:8000
# Set-ExecutionPolicy Unrestricted -Scope Process
from django.contrib import admin

# from django.forms import URLField
from django.forms import inlineformset_factory, BaseInlineFormSet
from django.forms import ModelForm
from .models import *
from .forms import *
# from django.contrib.admin.options import StackedInline, TabularInline




class ImportDataInline(admin.TabularInline):
    model = ImportData
    fields = ('id', 'data')
    extra = 0


class ImportDataSetAdmin(admin.ModelAdmin):
    inlines = [
        ImportDataInline
    ]
    list_display = ('description', 'id',  'status')


admin.site.register(ImportDataSet, ImportDataSetAdmin)


# @admin.register(ImportDataSet)
# class ImportDataSetAdmin(admin.ModelAdmin):
#     list_display = ('id', 'status', 'import_date', 'import_time')
#
# @admin.register(ImportData)
# class ImportDataAdmin(admin.ModelAdmin):
#     list_display = ( 'id', 'data')

@admin.register(ImportDataSetStatus)
class ImportDataSetStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_date', 'status', 'google_sheet_link')

# admin.site.register(OrderItem)

@admin.register(WarehouseActionType)
class WarehouseActionTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(WarehouseFlow)
class WarehouseFlowAdmin(admin.ModelAdmin):
    list_display = ('action_type', 'creation_date')


@admin.register(ItemPlace)
class ItemPlaceAdmin(admin.ModelAdmin):
    list_display = ('item', 'place', 'quantity', 'owner')


@admin.register(GeneralItem)
class GeneralItemAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'category')


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('obj_name', 'object_id', 'table_name', 'id',)

    def obj_name(self, obj):
        # дозволяє відобразити інформацію з іншої моделі, тобто Item - це
        # батьківська і стукаючи в потрібну табличку беремо потрібні дані
        table = apps.get_model('accounting', obj.table_name)
        obj_name = table.objects.get(pk=obj.object_id).name
        if obj_name:
            return obj_name
        else:
            None


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
