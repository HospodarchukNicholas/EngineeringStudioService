# Generated by Django 4.2.7 on 2023-11-09 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0010_generalitem_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemplace',
            name='warehouse_flow',
        ),
    ]
