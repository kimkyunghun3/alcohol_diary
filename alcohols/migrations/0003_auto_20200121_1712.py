# Generated by Django 3.0.2 on 2020-01-21 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alcohols', '0002_auto_20200120_1827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alcoholtype',
            old_name='Alcohol_name',
            new_name='alcohol_name',
        ),
    ]
