# Generated by Django 3.1.7 on 2021-06-17 14:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('conceptID', models.AutoField(primary_key=True, serialize=False)),
                ('conceptName', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'Concept',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('questionID', models.AutoField(primary_key=True, serialize=False)),
                ('example', models.CharField(max_length=100)),
                ('meaning', models.CharField(max_length=100)),
                ('translation', models.CharField(max_length=500)),
                ('concept', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question', to='questionRecord.concept')),
            ],
            options={
                'verbose_name': 'Questions',
                'verbose_name_plural': 'Questions',
                'db_table': 'Question',
            },
        ),
        migrations.CreateModel(
            name='SubConcept',
            fields=[
                ('subConceptID', models.AutoField(primary_key=True, serialize=False)),
                ('subConceptName', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'SubConcept',
            },
        ),
        migrations.CreateModel(
            name='Wrong',
            fields=[
                ('uerID', models.IntegerField(primary_key=True, serialize=False)),
                ('createTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updateTime', models.DateTimeField(auto_now=True)),
                ('count', models.CharField(default='0', max_length=100)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wrong', to='questionRecord.question')),
            ],
            options={
                'db_table': 'Wrong',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='subConcept1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question1', to='questionRecord.subconcept'),
        ),
        migrations.AddField(
            model_name='question',
            name='subConcept2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question2', to='questionRecord.subconcept'),
        ),
    ]
