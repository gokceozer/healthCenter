# Generated by Django 2.2.5 on 2020-03-19 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0006_auto_20200319_0144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='past_location',
            name='idn',
        ),
    ]