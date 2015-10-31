# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151031_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificado',
            name='tipo',
            field=models.CharField(default='palestra', max_length=15, choices=[(b'palestra', 'Palestra'), (b'curso-1', 'Curso 1'), (b'curso-2', 'Curso 2')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='certificado',
            name='arquivo',
            field=models.FileField(upload_to=core.models.upload_certificados),
        ),
    ]
