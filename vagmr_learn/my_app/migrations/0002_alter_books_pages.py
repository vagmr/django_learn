# Generated by Django 4.2.9 on 2024-01-23 08:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("my_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="books",
            name="pages",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(
                        1, message="Pages must be greater than 0"
                    )
                ]
            ),
        ),
    ]
