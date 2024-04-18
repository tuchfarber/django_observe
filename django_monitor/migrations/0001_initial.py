# Generated by Django 5.0.4 on 2024-04-09 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("method", models.CharField(max_length=10)),
                ("path", models.CharField(max_length=256)),
                ("status_code", models.IntegerField()),
                ("remote_addr", models.CharField(max_length=46)),
                ("user_agent", models.CharField(max_length=200)),
                ("timestamp", models.IntegerField()),
            ],
        ),
    ]
