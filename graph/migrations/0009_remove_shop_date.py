# Generated by Django 3.0.5 on 2020-05-05 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0008_auto_20200505_0731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='date',
        ),
    ]