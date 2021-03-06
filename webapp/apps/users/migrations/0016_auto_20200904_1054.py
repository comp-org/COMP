# Generated by Django 3.0.9 on 2020-09-04 10:54

from django.db import migrations, models
import django.db.models.deletion
import uuid
import webapp.apps.users.models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0015_remove_project_server_cost"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="callable_name",
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name="project",
            name="tech",
            field=models.CharField(
                choices=[
                    ("python-paramtools", "Python-ParamTools"),
                    ("dash", "Dash"),
                    ("bokeh", "Bokeh"),
                ],
                default="python-paramtools",
                max_length=64,
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="status",
            field=models.CharField(
                choices=[
                    ("live", "live"),
                    ("updating", "updating"),
                    ("pending", "pending"),
                    ("staging", "staging"),
                    ("requires fixes", "requires fixes"),
                ],
                default="live",
                max_length=32,
            ),
        ),
        migrations.CreateModel(
            name="EmbedApproval",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.CharField(max_length=256)),
                ("name", models.CharField(max_length=32)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="embed_approvals",
                        to="users.Profile",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="embed_approvals",
                        to="users.Project",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Deployment",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "short_id",
                    models.CharField(
                        default=webapp.apps.users.models.default_short_id, max_length=6
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("deleted_at", models.DateTimeField(null=True)),
                ("last_load_at", models.DateTimeField(auto_now_add=True)),
                ("last_ping_at", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(max_length=150, null=True)),
                ("tag", models.CharField(max_length=64, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("creating", "Creating"),
                            ("running", "Running"),
                            ("terminated", "Terminated"),
                        ],
                        default="creating",
                        max_length=32,
                    ),
                ),
                (
                    "embed_approval",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="deployments",
                        to="users.EmbedApproval",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="deployments",
                        to="users.Profile",
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="deployments",
                        to="users.Project",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cluster",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.URLField(max_length=64)),
                ("jwt_secret", models.CharField(max_length=512, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("deleted_at", models.DateTimeField(null=True)),
                (
                    "service_account",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="users.Profile",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="project",
            name="cluster",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="projects",
                to="users.Cluster",
            ),
        ),
    ]
