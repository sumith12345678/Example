# Generated by Django 4.1.6 on 2023-02-09 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
