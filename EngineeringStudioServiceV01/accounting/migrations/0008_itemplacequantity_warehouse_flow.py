# Generated by Django 4.2.7 on 2023-11-02 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0007_itemplacequantity_owner_warehouseactiontype_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemplacequantity',
            name='warehouse_flow',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.warehouseflow'),
        ),
    ]