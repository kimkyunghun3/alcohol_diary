# Generated by Django 3.0.2 on 2020-01-15 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_auto_20200115_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='main_image',
            field=models.ImageField(blank=True, upload_to='image_photos', verbose_name='메인 이미지'),
        ),
    ]
