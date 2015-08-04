# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.TextField(unique=True)),
                ('fullname', models.TextField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.BigIntegerField()),
                ('linkedin', models.TextField()),
                ('user_type', models.TextField()),
                ('user_interests', models.TextField()),
                ('education', models.TextField()),
                ('password', models.TextField()),
                ('slug', models.SlugField(default=b'', unique=True)),
            ],
        ),
    ]
