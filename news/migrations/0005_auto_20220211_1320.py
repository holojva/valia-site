# Generated by Django 3.1.5 on 2022-02-11 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20220204_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news_images/'),
        ),
        migrations.AlterField(
            model_name='commentaries',
            name='date',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2022, 2, 11, 13, 20, 6, 731021)),
        ),
    ]
