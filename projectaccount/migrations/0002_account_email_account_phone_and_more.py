# Generated by Django 4.2.6 on 2023-10-10 07:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projectaccount", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="email",
            field=models.EmailField(
                default=1, max_length=60, unique=True, verbose_name="email"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="account",
            name="phone",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="account",
            name="roll_number",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
