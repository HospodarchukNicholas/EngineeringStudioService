# Generated by Django 4.2.7 on 2023-11-10 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0016_shoppingcartitem_shoppingcart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcartitem',
            name='category',
        ),
        migrations.RemoveField(
            model_name='shoppingcartitem',
            name='supplier',
        ),
        migrations.DeleteModel(
            name='ShoppingCart',
        ),
        migrations.DeleteModel(
            name='ShoppingCartItem',
        ),
    ]
