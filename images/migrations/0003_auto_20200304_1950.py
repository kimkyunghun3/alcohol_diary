# Generated by Django 3.0.2 on 2020-03-04 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0002_diary_creator'),
        ('images', '0002_auto_20200220_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='diary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diaries.Diary'),
        ),
    ]
