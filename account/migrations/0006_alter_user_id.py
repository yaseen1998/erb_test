# Generated by Django 4.0.5 on 2022-06-16 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_account_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='b0234d6f6b', editable=False, max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
