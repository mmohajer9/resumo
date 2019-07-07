# Generated by Django 2.2.2 on 2019-07-07 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0002_userdetail_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='primary_skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_who_have_this_as_primary', to='weblog.Skill'),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='secondary_skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_who_have_this_as_secondary', to='weblog.Skill'),
        ),
    ]