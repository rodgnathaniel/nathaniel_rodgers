# Generated by Django 2.1.5 on 2019-03-08 22:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('boat', '0014_auto_20190308_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2019, 3, 8, 22, 1, 4, 744483, tzinfo=utc)),
            preserve_default=False,
        ),
    ]