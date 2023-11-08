# Set-ExecutionPolicy Unrestricted -Scope Process
# .\venv\Scripts\activate
# from accounting.models import read_google_sheet
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Avg, Count, Min, Sum
from django.apps import apps
import json
import pandas as pd
import openpyxl
import gspread
import os
from django.apps import apps
from engineering_concept_studio.models import *


# отримати модель маючи назву
# apps.get_model('accounting', table_name)

def read_google_sheet(url):
    # Get the Google Sheet API service
    g = gspread.service_account()

    # Open the Google Sheet by URL
    sh = g.open_by_url(url)

    # Get the first worksheet
    worksheet = sh.sheet1

    # Get all the data from the worksheet
    data = worksheet.get_all_values()

    # Extract column headers
    headers = data[0]

    # Convert data to a list of dictionaries
    data_as_dicts = []

    for row in data[1:]:
        row_dict = dict(zip(headers, row))
        print(row)
        print(row_dict)
        data_as_dicts.append(row_dict)

    return data_as_dicts


# class PlaceType(models.Model):
#     # може бути фізичним місцем або проектор і тд.
#     name = models.CharField(max_length=255, unique=True)
#     description = models.TextField(blank=True)
#
#     def __str__(self):
#         return self.name


class Place(models.Model):
    name = models.CharField(max_length=255, unique=True)
    # type = models.ForeignKey(PlaceType, null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    # посилання на свій же клас дозволяє зробити гнучку структуру фізичного розташування
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ImportDataSetStatus(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)

    def __str__(self):
        return self.name


class ImportDataSet(models.Model):
    import_date = models.DateField(auto_now_add=True, blank=True)
    import_time = models.TimeField(auto_now_add=True, blank=True)
    description = models.TextField(blank=True)
    status = models.ForeignKey(ImportDataSetStatus, on_delete=models.CASCADE, blank=False)
    google_sheet_link = models.URLField(blank=False, max_length=255)

    def save(self, *args, **kwargs):
        super(ImportDataSet, self).save(*args, **kwargs)
        sheet_data = read_google_sheet(self.google_sheet_link)
        for row in sheet_data:
            ImportData.objects.update_or_create(data_set=self, data=row)

        status = ImportDataSetStatus.objects.filter(name='Warehouse integration').first()
        if self.status == status:
            items_to_integrate = ImportData.objects.filter(data_set=self)
            for item in items_to_integrate:
                name = item.data['name']
                gi = GeneralItem.objects.update_or_create(name=name)
                place = item.data['place']
                if not place:
                    place = 'Warehouse'
                place = Place.objects.update_or_create(name=place)
                # item = Item.objects.get(object_id=)
                # quantity = str(item.data['quantity'])
                # ItemPlace.objects.update_or_create(item=i, place=place, quantity=quantity)



    def __str__(self):
        return f'{self.status} - {self.import_date}'


class ImportData(models.Model):
    data_set = models.ForeignKey(ImportDataSet, on_delete=models.CASCADE)
    data = models.JSONField()

    def __str__(self):
        return json.dumps(self.data)


class Attribute(models.Model):
    # для моделі GeneralItem створюємо необмежену зількість додаткових полів
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}: {self.value}'


class ItemCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class GeneralItem(models.Model):
    name = models.CharField(max_length=255, unique=True)
    attributes = models.ManyToManyField(Attribute, blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(ItemCategory, on_delete=models.SET_NULL, blank=True, null=True)

    def save(self, *args, **kwargs):
        super(GeneralItem, self).save(*args, **kwargs)
        table_name = self._meta.model_name
        object_id = self.pk
        # Створюємо новий Item
        Item.objects.update_or_create(object_id=object_id, table_name=table_name)

    def __str__(self):
        return self.name


class Item(models.Model):
    # модель в яку записується всі існуючі компоненти, тобто це дозволяє різні
    # таблиці зібрати в одному місці і отримати до них доступ
    object_id = models.PositiveIntegerField()
    table_name = models.CharField(max_length=255, blank=False)

    class Meta:
        unique_together = (('object_id', 'table_name',),)

    def __str__(self):
        table = apps.get_model('accounting', self.table_name)
        obj = table.objects.get(pk=self.object_id)
        return f'{obj.name}'

    def save(self, *args, **kwargs):
        super(Item, self).save(*args, **kwargs)
        # ItemPlace.objects.update_or_create(item=self, place='Нерозміщено', quantity=0, owner='Defir')


class OrderStatus(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_date = models.DateField(auto_now_add=True, blank=True)
    order_time = models.TimeField(auto_now_add=True, blank=True)
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)
    google_sheet_link = models.URLField(blank=True, max_length=255)

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)
        # table_name = self._meta.model_name
        # object_id = self.pk
        # Створюємо новий Item
        # Item.objects.update_or_create(object_id=object_id, table_name=table_name)

    def __str__(self):
        return f'{self.status} - {self.order_date}'


class WarehouseActionType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class WarehouseFlow(models.Model):
    # записуємо дії які робимо
    action_type = models.ForeignKey(WarehouseActionType, null=True, blank=True, on_delete=models.CASCADE)
    creation_date = models.DateField(auto_now_add=True, blank=True)
    creation_time = models.TimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f'{self.action_type}: {self.creation_date}'





class Supplier(models.Model):
    name = models.CharField(max_length=255, blank=False)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    # модель зв'язує один компонент і замовлення
    item = models.ForeignKey(Item, null=True, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.CASCADE, blank=True)
    quantity = models.PositiveIntegerField(blank=False, default=1)
    product_link = models.URLField(blank=True)
    invoice = models.URLField(blank=True)

    class Meta:
        unique_together = (('item', 'order', 'supplier'),)

    def __str__(self):
        return f'Item: {self.item}, Object id: {self.order}'


class Owner(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ItemPlace(models.Model):
    # warehouse_flow = models.ForeignKey(WarehouseFlow, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(blank=False, default=0)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, blank=True)

    class Meta:
        unique_together = (('item', 'place', 'owner',),)

    def get_total_quantity(item):
        # метод get_total_quantity дозволяє отримати кількість всіх Item в одному місці
        return ItemPlace.objects.filter(item=item).aggregate(Sum('quantity'))['quantity__sum']

    def __str__(self):
        return f'Item: {self.item}, Object place: {self.place}'


class FastenerSize(models.Model):
    size = models.CharField(max_length=255, blank=False, unique=True)

    def __str__(self):
        return self.size


class ItemMaterial(models.Model):
    name = models.CharField(max_length=255, unique=True, )
    short_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def normalize_name(self):
        self.name = self.name.lower()
        self.short_name = self.short_name.upper()

    def save(self, *args, **kwargs):
        self.normalize_name()
        super(ItemMaterial, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Standard(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def normalize_name(self):
        self.name = self.name.upper()

    def save(self, *args, **kwargs):
        self.normalize_name()
        super(Standard, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class StandardCode(models.Model):
    # name = models.CharField(max_length=255, unique=True)
    standard = models.ForeignKey(Standard, on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    @property
    def name(self):
        return f'{self.standard} {self.code}'

    def __str__(self):
        return self.name


class GradeClass(models.Model):
    grade = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return str(self.grade)


class Nut(models.Model):
    standard = models.ForeignKey(StandardCode, on_delete=models.CASCADE, blank=False)
    size = models.ForeignKey(FastenerSize, on_delete=models.CASCADE, blank=False)
    material = models.ForeignKey(ItemMaterial, on_delete=models.CASCADE, blank=False)
    grade = models.ForeignKey(GradeClass, on_delete=models.PROTECT, blank=False)

    def save(self, *args, **kwargs):
        super(Nut, self).save(*args, **kwargs)
        table_name = self._meta.model_name
        object_id = self.pk
        # Створюємо новий Item
        Item.objects.update_or_create(object_id=object_id, table_name=table_name)

    @property
    def name(self):
        return f'Nut - {str(self.size)} - {str(self.standard)} - {self.material.short_name} - {str(self.grade)}'

    class Meta:
        unique_together = (('standard', 'material', 'size', 'grade'),)

    def __str__(self):
        return self.name


class Bolt(models.Model):
    size = models.ForeignKey(FastenerSize, on_delete=models.CASCADE, blank=False)
    standard = models.ForeignKey(StandardCode, on_delete=models.CASCADE, blank=False)
    length = models.PositiveIntegerField()
    material = models.ForeignKey(ItemMaterial, on_delete=models.CASCADE, blank=False)
    grade = models.ForeignKey(GradeClass, on_delete=models.PROTECT, blank=False)

    def save(self, *args, **kwargs):
        super(Bolt, self).save(*args, **kwargs)
        table_name = self._meta.model_name
        object_id = self.pk
        # Створюємо новий Item
        Item.objects.update_or_create(object_id=object_id, table_name=table_name)

    @property
    def name(self):
        return f'Bolt - {str(self.size)} - {str(self.standard)} - L{str(self.length)} - {self.material.short_name} - {str(self.grade)}'

    class Meta:
        unique_together = (('size', 'standard', 'length', 'material', 'grade'),)

    def __str__(self):
        return self.name

# реєструємо всі наші бази щоб потім знати яку вибрати з конкретного класу маючи тільки об'єкт
# class ModelRegistry:
#     model_classes = {}
#
#     def register(self, model_class):
#         table_name = model_class._meta
#         self.model_classes[table_name] = model_class
#
#     def get_model_classes(self, model_name):
#         return self.model_classes(model_name)
# ModelRegistry().register(Item)
