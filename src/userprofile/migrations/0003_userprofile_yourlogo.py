# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_remove_userprofile_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='yourlogo',
            field=models.FileField(upload_to=b'logos/%Y/%m/%d', blank=True),
        ),
    ]
