# Generated by Django 4.2.9 on 2024-02-01 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_course"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="创建时间"
            ),
        ),
    ]
