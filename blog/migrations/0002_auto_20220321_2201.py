# Generated by Django 3.2.12 on 2022-03-21 13:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iName', models.CharField(max_length=20)),
                ('genre', models.CharField(max_length=10)),
                ('stock', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField(default=django.utils.timezone.now)),
                ('price', models.PositiveIntegerField()),
                ('volume', models.PositiveSmallIntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.item')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sName', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='price',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.shop'),
        ),
    ]