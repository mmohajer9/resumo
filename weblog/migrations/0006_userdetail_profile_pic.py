# Generated by Django 2.2.2 on 2019-07-16 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0005_auto_20190716_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]
