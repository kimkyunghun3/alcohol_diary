# Generated by Django 3.0.2 on 2020-01-22 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alcohols', '0003_auto_20200121_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='alcoholrecord',
            name='alcohol',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='alcohols.Alcohol'),
        ),
    ]
