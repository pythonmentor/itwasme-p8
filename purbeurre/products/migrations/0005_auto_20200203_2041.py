# Generated by Django 3.0.2 on 2020-02-03 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200203_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_nutriscore',
            field=models.CharField(max_length=3),
        ),
    ]