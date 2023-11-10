# python manage.py runserver 192.168.0.214:8000
# Set-ExecutionPolicy Unrestricted -Scope Process
from django.contrib import admin
# from django.forms import URLField
from django.forms import inlineformset_factory, BaseInlineFormSet
from django.forms import ModelForm
from .models import *
from .forms import *
# from django.contrib.admin.options import StackedInline, TabularInline
admin.site.site_header = 'DefirWarehouse_v0.2'
admin.site.site_title = 'DefirWarehouse_v0.2'

# @admin.action(description="Warehouse Integration")
# def WarehouseIntegration(modeladmin, request, queryset):
#     status = ImportDataSetStatus.objects.filter(name='Warehouse integration').first()
#     queryset.update(status=status)




class ShoppingCartItemInline(admin.TabularInline):
    model = ShoppingCartItem
    fields = ('id', )


class ShoppingCartAdmin(admin.ModelAdmin):
    inlines = [
        ShoppingCartItemInline
    ]
    list_display = ('purpose', 'status', 'id')

admin.site.register(ShoppingCart, ShoppingCartAdmin)
admin.site.register(ShoppingCartItem)



class ImportDataInline(admin.TabularInline):
    model = ImportData
    fields = ('id', )


class ImportDataSetAdmin(admin.ModelAdmin):
    inlines = [
        ImportDataInline
    ]
    list_display = ( 'description', 'status', 'id' )
    # actions = [WarehouseIntegration]

admin.site.register(ImportDataSet, ImportDataSetAdmin)






@admin.register(ItemPlace)
class ItemPlaceAdmin(admin.ModelAdmin):
    list_display = ('item', 'place', 'quantity', 'owner', 'id')


@admin.register(GeneralItem)
class GeneralItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'description')


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    # list_display = ('name', 'value')
    def get_model_perms(self, request):
        return {}



@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'object_id', 'item_places', 'total_quantity')

    def item_name(self, obj):
        # дозволяє відобразити інформацію з іншої моделі, тобто Item - це
        # батьківська і стукаючи в потрібну табличку беремо потрібні дані
        table = apps.get_model('accounting', obj.table_name)
        obj_name = table.objects.get(pk=obj.object_id).name
        if obj_name:
            return obj_name
        else:
            None
    def item_places(self, obj):
        item_places = ItemPlace.objects.filter(item=obj.id)
        places_name = item_places.values_list('place__name', flat=True)
        place_quantity = item_places.values_list('quantity', flat=True)

        places_info = zip(item_places.values_list('place__name', flat=True),
                          item_places.values_list('quantity', flat=True))
        places_str = ', '.join([f"{name}: {quantity} pcs" for name, quantity in places_info])
        if places_str:
            return places_str

    def total_quantity(self, obj):
        item_places = ItemPlace.objects.filter(item=obj.id)
        total_quantity = item_places.aggregate(total_quantity=Sum('quantity'))['total_quantity']
        return total_quantity
    # def total_quantity(self, obj):
    #     item_total_quantity = ItemPlace.get_total_quantity(obj)
    #     if item_total_quantity:
    #         return item_total_quantity

# @admin.register(Bolt)
# class BoltAdmin(admin.ModelAdmin):
#     list_display = ('name', 'id',)
#
# @admin.register(Nut)
# class BoltAdmin(admin.ModelAdmin):
#     list_display = ('name', 'id',)

# @admin.register(ImportDataSetStatus)
# class ImportDataSetStatusAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', )


# admin.site.register(FastenerSize)
# admin.site.register(OrderStatus)
# admin.site.register(GradeClass)
# admin.site.register(ItemMaterial)
# admin.site.register(Place)
# admin.site.register(StandardCode)
# admin.site.register(Standard)
# admin.site.register(ItemCategory)
# admin.site.register(Owner)

# @admin.register(ItemCategory)
# class ItemCategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'id',)


# @admin.register(StandardCode)
# class StandardCodeAdmin(admin.ModelAdmin):
#     list_display = ('name', 'id', 'description',)


# @admin.register(Standard)
# class StandardAdmin(admin.ModelAdmin):
#     list_display = ('name', 'id', 'description',)


# @admin.register(ItemMaterial)
# class ItemMaterialAdmin(admin.ModelAdmin):
#     list_display = ('name', 'id', 'short_name', 'description',)


# @admin.register(FastenerSize)
# class FastenerSizeAdmin(admin.ModelAdmin):
#     list_display = ('size', 'id',)

# @admin.register(Place)
# class PlaceAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'parent', 'id',)

# @admin.register(GradeClass)
# class GradeClassAdmin(admin.ModelAdmin):
#     list_display = ('grade', 'id',)


# @admin.register(OrderStatus)
# class OrderStatusAdmin(admin.ModelAdmin):
#     list_display = ('name', 'id',)

# @admin.register(WarehouseFlow)
# class WarehouseFlowAdmin(admin.ModelAdmin):
#     list_display = ('action_type', 'creation_date')

# @admin.register(ImportDataSet)
# class ImportDataSetAdmin(admin.ModelAdmin):
#     list_display = ('id', 'status', 'import_date', 'import_time')
#
# @admin.register(ImportData)
# class ImportDataAdmin(admin.ModelAdmin):
#     list_display = ( 'id', 'data')



# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('id', 'order_date', 'status', 'google_sheet_link')

# admin.site.register(OrderItem)

# @admin.register(WarehouseActionType)
# class WarehouseActionTypeAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description')
