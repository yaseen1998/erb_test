# Generated by Django 4.0.5 on 2022-06-19 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='5d543deaff', editable=False, max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
