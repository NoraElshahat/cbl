# Generated by Django 3.1.5 on 2021-01-17 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='faculty.faculty')),
            ],
        ),
    ]
