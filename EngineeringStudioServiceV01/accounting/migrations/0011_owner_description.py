# Generated by Django 4.2.7 on 2023-11-02 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0010_alter_itemplacequantity_warehouse_flow'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
