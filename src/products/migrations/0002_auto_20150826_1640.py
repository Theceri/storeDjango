# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='owner',
            field=models.CharField(default=datetime.datetime(2015, 8, 26, 16, 40, 28, 564252, tzinfo=utc), max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='products',
            name='photo',
            field=models.FileField(upload_to=b'puloads/%Y/%m/%d'),
        ),
    ]
