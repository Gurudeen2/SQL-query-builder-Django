# Generated by Django 3.0.5 on 2021-01-19 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='DATE_CREATED',
            field=models.DateField(blank=True),
        ),
    ]
