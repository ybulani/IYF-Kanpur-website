# Generated by Django 3.0.7 on 2020-06-17 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20200617_0040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='college',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='graduation',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='stream',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='year_of_passout',
        ),
    ]