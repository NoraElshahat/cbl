# Generated by Django 3.1.5 on 2021-01-18 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='contructured_at',
            field=models.DateTimeField(blank=True),
        ),
    ]
