# Generated by Django 5.1.2 on 2025-01-08 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("psy_faust", "0007_rename_email_contacts_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="faq",
            name="title",
            field=models.CharField(max_length=150, verbose_name="Вопрос"),
        ),
    ]
