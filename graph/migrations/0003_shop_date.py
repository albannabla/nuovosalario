# Generated by Django 3.0.5 on 2020-05-05 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0002_auto_20200429_0653'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='date',
            field=models.DateField(),
        ),
    ]
