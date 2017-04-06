# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsPut', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='savePage',
            new_name='Page',
        ),
    ]
