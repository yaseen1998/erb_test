# Generated by Django 4.0.5 on 2022-06-19 08:03

from django.db import migrations, models
import django.db.models.deletion
import fake_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('module', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='models', to='fake_app.app')),
            ],
            options={
                'unique_together': {('app', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255, validators=[fake_app.models.is_valid_field])),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='fake_app.model')),
            ],
            options={
                'unique_together': {('model', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='fake_app.field')),
            ],
            options={
                'unique_together': {('field', 'name')},
            },
        ),
    ]
