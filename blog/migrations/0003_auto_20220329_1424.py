# Generated by Django 3.2.12 on 2022-03-29 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220321_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='under',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='stock',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
