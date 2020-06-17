# Generated by Django 3.0.7 on 2020-06-17 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_devotional_education_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devotional',
            name='started_16japa',
            field=models.DateField(blank=True, verbose_name='Chanting 16 rounds since (Month and Year)'),
        ),
        migrations.AlterField(
            model_name='devotional',
            name='started_japa',
            field=models.DateField(verbose_name='Chanting Since (Month and Year)'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(),
        ),
    ]
