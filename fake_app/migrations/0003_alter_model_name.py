# Generated by Django 4.0.5 on 2022-06-19 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fake_app', '0002_alter_model_unique_together_alter_model_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
