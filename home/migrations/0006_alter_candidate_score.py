# Generated by Django 4.2.4 on 2023-08-11 11:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0005_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="candidate",
            name="score",
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
    ]
