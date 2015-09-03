# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('price', models.CharField(max_length=150)),
                ('category', models.CharField(max_length=150, choices=[(b'electronics', b'electronics'), (b'fashion', b'fashion')])),
                ('description', models.TextField(max_length=1000, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('photo', models.FileField(upload_to=b'documents/%Y/%m/%d')),
            ],
        ),
    ]
