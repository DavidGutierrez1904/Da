# Generated by Django 3.2.6 on 2021-09-06 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210905_2208'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['id'], 'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AlterModelTable(
            name='products',
            table='product',
        ),
    ]
