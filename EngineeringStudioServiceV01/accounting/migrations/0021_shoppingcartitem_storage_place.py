# Generated by Django 4.2.7 on 2023-11-13 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0020_alter_shoppingcart_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcartitem',
            name='storage_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounting.place'),
        ),
    ]