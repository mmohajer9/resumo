# Generated by Django 2.2.2 on 2019-07-21 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0020_auto_20190720_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
