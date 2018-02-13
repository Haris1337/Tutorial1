# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='time_of_comment',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
