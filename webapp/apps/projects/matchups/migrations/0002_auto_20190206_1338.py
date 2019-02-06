# Generated by Django 2.1.5 on 2019-02-06 18:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [("matchups", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="matchupsrun",
            name="creation_date",
            field=models.DateTimeField(
                default=datetime.datetime(2015, 1, 1, 5, 0, tzinfo=utc)
            ),
        ),
        migrations.AlterField(
            model_name="matchupsrun",
            name="exp_comp_datetime",
            field=models.DateTimeField(
                default=datetime.datetime(2015, 1, 1, 5, 0, tzinfo=utc)
            ),
        ),
    ]