# Generated by Django 4.0.5 on 2022-06-19 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='032ecb8613', editable=False, max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]