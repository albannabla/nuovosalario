# Generated by Django 3.0.5 on 2020-05-05 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0004_auto_20200505_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='date',
            field=models.DateField(default='2020-03-30'),
        ),
    ]
