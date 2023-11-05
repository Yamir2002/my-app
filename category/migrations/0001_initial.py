# Generated by Django 3.1.6 on 2023-06-19 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sb1', models.CharField(blank=True, default='', max_length=50)),
                ('sb2', models.CharField(blank=True, default='', max_length=50)),
                ('sb3', models.CharField(blank=True, default='', max_length=50)),
                ('sb4', models.CharField(blank=True, default='', max_length=50)),
                ('sb5', models.CharField(blank=True, default='', max_length=50)),
                ('sb6', models.CharField(blank=True, default='', max_length=50)),
            ],
        ),
    ]
