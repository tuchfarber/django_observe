# Generated by Django 5.0.3 on 2024-04-17 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("django_monitor", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="timestamp",
            field=models.DateTimeField(),
        ),
    ]
