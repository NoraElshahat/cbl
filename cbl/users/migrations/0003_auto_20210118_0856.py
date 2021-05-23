# Generated by Django 3.1.5 on 2021-01-18 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_cbluser_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cbluser',
            old_name='name',
            new_name='first',
        ),
        migrations.AddField(
            model_name='cbluser',
            name='last',
            field=models.CharField(default='CBL', max_length=250),
            preserve_default=False,
        ),
    ]
