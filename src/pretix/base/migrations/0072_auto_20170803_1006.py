# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-03 10:06
from __future__ import unicode_literals

from django.db import migrations, models


def set_priority(app, schema_editor):
    wles = app.get_model('pretixbase', 'WaitingListEntry')
    wles.objects.filter(voucher__isnull=True).update(priority=10)


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0071_auto_20170729_1616'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='waitinglistentry',
            options={'ordering': ['-priority', 'created'], 'verbose_name': 'Waiting list entry', 'verbose_name_plural': 'Waiting list entries'},
        ),
        migrations.AddField(
            model_name='waitinglistentry',
            name='priority',
            field=models.PositiveIntegerField(help_text='Priority of this entry.', null=True, verbose_name='Priority'),
        ),
        migrations.RunPython(
            set_priority, migrations.RunPython.noop
        ),
    ]