# Generated by Django 2.2.2 on 2019-07-07 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0005_auto_20190707_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPostLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('blogPost_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weblog.BlogPost')),
            ],
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='weblog.Comment')),
            ],
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]