# Generated by Django 3.0.5 on 2020-05-05 07:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0009_remove_shop_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
