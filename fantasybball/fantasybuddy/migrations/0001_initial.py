# Generated by Django 4.1.5 on 2023-01-26 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("position", models.CharField(max_length=5)),
                ("status", models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name="PlayerWaiverStatus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("league", models.PositiveIntegerField()),
                ("status", models.CharField(max_length=10)),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fantasybuddy.player",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PlayerStats",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timeline", models.CharField(max_length=5)),
                ("rank", models.PositiveIntegerField()),
                (
                    "field_goal_attempts",
                    models.DecimalField(decimal_places=2, max_digits=4),
                ),
                (
                    "field_goals_made",
                    models.DecimalField(decimal_places=2, max_digits=4),
                ),
                ("ft_attempts", models.DecimalField(decimal_places=2, max_digits=4)),
                ("ft_made", models.DecimalField(decimal_places=2, max_digits=4)),
                ("three_pt_made", models.DecimalField(decimal_places=2, max_digits=4)),
                ("points", models.DecimalField(decimal_places=2, max_digits=4)),
                ("rebounds", models.DecimalField(decimal_places=2, max_digits=4)),
                ("assists", models.DecimalField(decimal_places=2, max_digits=4)),
                ("steals", models.DecimalField(decimal_places=2, max_digits=4)),
                ("blocks", models.DecimalField(decimal_places=2, max_digits=4)),
                ("tos", models.DecimalField(decimal_places=2, max_digits=4)),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fantasybuddy.player",
                    ),
                ),
            ],
        ),
    ]