# Generated by Django 3.0.5 on 2020-04-29 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0007_auto_20200429_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.FloatField(default=0),
        ),
    ]
