# Generated by Django 5.1.7 on 2025-03-21 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_service_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='services', verbose_name='imágen'),
        ),
    ]
