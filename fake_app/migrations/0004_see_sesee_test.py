# Generated by Django 4.0.5 on 2022-06-20 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fake_app', '0003_alter_model_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='See',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'See',
            },
        ),
        migrations.CreateModel(
            name='Sesee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'Sesee',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField()),
            ],
        ),
    ]