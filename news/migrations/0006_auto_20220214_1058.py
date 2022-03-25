# Generated by Django 3.1.5 on 2022-02-14 10:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20220211_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image_thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='news_images/'),
        ),
        migrations.AlterField(
            model_name='commentaries',
            name='date',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2022, 2, 14, 10, 58, 5, 303601)),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, default='news_images/default.webp', null=True, upload_to='news_images/'),
        ),
    ]