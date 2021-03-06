# Generated by Django 3.0.6 on 2020-05-30 08:30

import django.core.validators
from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200512_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='college',
            field=models.CharField(choices=[('iitbhu', 'IIT BHU'), ('iitk', 'IIT Kanpur'), ('bhu', 'BHU'), ('nit', 'NIT ALD'), ('iiit', 'IIIT ALD'), ('hbtu', 'HBTU'), ('iet', 'IET'), ('csjm', 'CSJM'), ('aith', 'AITH'), ('gcti', 'GCTI'), ('psit', 'PSIT'), ('rec', 'REC-Bijnore'), ('other', 'Other')], max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='graduation',
            field=models.CharField(choices=[('btech', 'B.Tech'), ('Be', 'BE'), ('Bsc', 'B.Sc.'), ('Dip', 'Diploma')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='stream',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='year_of_passout',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1960), user.models.max_value_current_year], verbose_name='Year of Passout'),
        ),
    ]
