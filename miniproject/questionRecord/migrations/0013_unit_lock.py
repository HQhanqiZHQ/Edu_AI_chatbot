# Generated by Django 3.1.7 on 2021-09-30 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionRecord', '0012_auto_20210831_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='lock',
            field=models.BooleanField(default=1),
        ),
    ]
