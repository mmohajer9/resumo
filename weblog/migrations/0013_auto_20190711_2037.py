# Generated by Django 2.2.2 on 2019-07-11 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0012_auto_20190709_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]