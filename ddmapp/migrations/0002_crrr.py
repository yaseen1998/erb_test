# Generated by Django 4.0.5 on 2022-06-19 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddmapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crrr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Crrr',
                'db_table': 'ddmapp_crrr',
            },
        ),
    ]