# Generated by Django 3.1.5 on 2021-01-18 07:55

from django.db import migrations, models
import time


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0004_auto_20210118_0755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='code',
            field=models.CharField(default=time.time, max_length=250),
        ),
    ]