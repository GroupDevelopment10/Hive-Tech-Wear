# Generated by Django 4.2.4 on 2023-09-04 01:15

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('price', models.FloatField(verbose_name='Price')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='Product image')),
                ('type', models.CharField(max_length=800, verbose_name='Type')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_category', to='categories.category')),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
