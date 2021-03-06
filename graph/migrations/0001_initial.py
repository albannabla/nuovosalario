# Generated by Django 3.0.5 on 2020-04-29 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('webid', models.CharField(max_length=30)),
                ('link', models.URLField(blank=True, db_index=True, max_length=128, unique=True)),
                ('price', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=30)),
                ('pricepersqm', models.FloatField(max_length=30)),
            ],
        ),
    ]
