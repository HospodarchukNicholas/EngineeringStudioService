# Generated by Django 4.2.7 on 2023-11-04 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FastenerSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GradeClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('table_name', models.CharField(max_length=255)),
            ],
            options={
                'unique_together': {('object_id', 'table_name')},
            },
        ),
        migrations.CreateModel(
            name='ItemMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('short_name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlaceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='WarehouseActionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='WarehouseFlow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('creation_time', models.TimeField(auto_now_add=True)),
                ('action_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.warehouseactiontype')),
            ],
        ),
        migrations.CreateModel(
            name='StandardCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.standard')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.place')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.placetype')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(auto_now_add=True)),
                ('order_time', models.TimeField(auto_now_add=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.orderstatus')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.itemcategory')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('attributes', models.ManyToManyField(blank=True, to='accounting.attribute')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_link', models.URLField(blank=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.item')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.order')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.supplier')),
            ],
            options={
                'unique_together': {('item', 'order', 'supplier')},
            },
        ),
        migrations.CreateModel(
            name='Nut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounting.gradeclass')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.itemmaterial')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.fastenersize')),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.standardcode')),
            ],
            options={
                'unique_together': {('standard', 'material', 'size', 'grade')},
            },
        ),
        migrations.CreateModel(
            name='ItemPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.item')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.owner')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.place')),
                ('warehouse_flow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.warehouseflow')),
            ],
            options={
                'unique_together': {('item', 'place', 'owner')},
            },
        ),
        migrations.CreateModel(
            name='Bolt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.PositiveIntegerField()),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounting.gradeclass')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.itemmaterial')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.fastenersize')),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.standardcode')),
            ],
            options={
                'unique_together': {('size', 'standard', 'length', 'material', 'grade')},
            },
        ),
    ]
