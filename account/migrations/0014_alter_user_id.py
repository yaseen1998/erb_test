# Generated by Django 4.0.5 on 2022-06-19 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='c97f9de7c0', editable=False, max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]