# Generated by Django 2.1.7 on 2019-03-16 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [("users", "0001_initial"), ("comp", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="simulation",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="sims",
                to="users.Profile",
            ),
        ),
        migrations.AddField(
            model_name="simulation",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="sims",
                to="users.Project",
            ),
        ),
        migrations.AddField(
            model_name="simulation",
            name="sponsor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="sponsored_sims",
                to="users.Profile",
            ),
        ),
        migrations.AddField(
            model_name="inputs",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="sim_params",
                to="users.Project",
            ),
        ),
    ]
