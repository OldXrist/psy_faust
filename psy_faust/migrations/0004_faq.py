# Generated by Django 5.1.2 on 2024-10-21 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("psy_faust", "0003_alter_qualifications_img"),
    ]

    operations = [
        migrations.CreateModel(
            name="FAQ",
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
                ("title", models.CharField(max_length=50, verbose_name="Вопрос")),
                (
                    "content",
                    models.TextField(max_length=500, verbose_name="Содержание"),
                ),
            ],
        ),
    ]