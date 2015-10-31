# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150702_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('arquivo', models.FileField(upload_to=b'uploads/certificados')),
            ],
        ),
        migrations.RemoveField(
            model_name='participante',
            name='certificado',
        ),
        migrations.AddField(
            model_name='certificado',
            name='participante',
            field=models.ForeignKey(to='core.Participante'),
        ),
    ]
