# Generated by Django 5.1.2 on 2024-10-21 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("psy_faust", "0002_alter_qualifications_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="qualifications",
            name="img",
            field=models.ImageField(upload_to="static/img/", verbose_name="Картинка"),
        ),
    ]
