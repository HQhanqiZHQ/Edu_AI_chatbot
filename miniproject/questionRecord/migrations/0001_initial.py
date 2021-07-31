# Generated by Django 3.1.7 on 2021-07-29 17:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = False

    dependencies = [
    ]

    operations = [
        migrations.AddField(
            model_name='CommonUser',
            name='continueCheckDays',
            field=models.IntegerField(null=False, blank=False, default=0),
        ),
        migrations.AddField(
            model_name='CommonUser',
            name='lastCheckDate',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='CommonUser',
            name='conSign',
            field=models.IntegerField(default=0)
        ),
        migrations.AddField(
            model_name='CommonUser',
            name='level3Lock',
            field=models.BooleanField(default=False)
        ),
        migrations.AddField(
            model_name='CommonUser',
            name='level4Lock',
            field=models.BooleanField(default=False)
        ),
    ]
