# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('imgNm', models.ImageField(upload_to='%Y/%m/%d')),
                ('description', models.TextField(blank=True, max_length=500)),
                ('pub_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
