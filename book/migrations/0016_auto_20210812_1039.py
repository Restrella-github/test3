# Generated by Django 2.2.10 on 2021-08-12 08:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0015_auto_20210811_2303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrowrecord',
            old_name='status',
            new_name='open_or_close',
        ),
        migrations.AlterField(
            model_name='borrowrecord',
            name='end_day',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 19, 8, 39, 11, 212961, tzinfo=utc)),
        ),
    ]