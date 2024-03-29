# Generated by Django 4.2.9 on 2024-01-24 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Room",
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
                ("r_code", models.CharField(default="", max_length=12, unique=True)),
                ("host", models.CharField(max_length=50, unique=True)),
                ("guest_can_pause", models.BooleanField(default=False)),
                ("votes_to_skip", models.IntegerField(default=1)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
