# Generated by Django 3.0.2 on 2020-01-15 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('main_image', models.ImageField(blank=True, upload_to='', verbose_name='메인 이미지')),
            ],
        ),
    ]