# Generated by Django 2.0.4 on 2018-05-15 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20180515_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='observation',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='pipelineconfiguration',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='session',
            name='owner',
        ),
    ]
