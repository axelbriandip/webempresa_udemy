# Generated by Django 5.1.7 on 2025-03-20 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='título')),
                ('subtitle', models.CharField(max_length=100, verbose_name='subtítulo')),
                ('description', models.TextField(max_length=200, verbose_name='descripción')),
                ('image', models.ImageField(upload_to='', verbose_name='imágen')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'servicio',
                'verbose_name_plural': 'servicios',
                'ordering': ['-created'],
            },
        ),
    ]
