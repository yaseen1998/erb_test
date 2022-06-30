# Generated by Django 4.0.5 on 2022-06-16 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(default='3481b4200b', editable=False, max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
