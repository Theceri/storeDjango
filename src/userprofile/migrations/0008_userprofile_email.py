# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_remove_userprofile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default=datetime.datetime(2015, 8, 26, 16, 10, 16, 685099, tzinfo=utc), max_length=b'150'),
            preserve_default=False,
        ),
    ]
