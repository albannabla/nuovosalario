# Generated by Django 3.0.5 on 2020-05-19 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0012_auto_20200519_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='price',
            field=models.CharField(max_length=95),
        ),
    ]
