# Generated by Django 3.0.5 on 2020-05-14 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0003_auto_20200514_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clubdeportivo',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
