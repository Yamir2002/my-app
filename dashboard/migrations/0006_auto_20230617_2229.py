# Generated by Django 3.1.6 on 2023-06-17 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_product_featured_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]