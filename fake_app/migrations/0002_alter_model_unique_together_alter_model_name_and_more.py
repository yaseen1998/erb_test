# Generated by Django 4.0.5 on 2022-06-19 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fake_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='model',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='model',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.RemoveField(
            model_name='model',
            name='app',
        ),
    ]
