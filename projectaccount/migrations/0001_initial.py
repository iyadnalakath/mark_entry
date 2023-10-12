# Generated by Django 4.2.6 on 2023-10-10 07:05

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("username", models.CharField(max_length=60, unique=True)),
                (
                    "date_joined",
                    models.DateTimeField(auto_now_add=True, verbose_name="date joined"),
                ),
                (
                    "last_login",
                    models.DateTimeField(auto_now=True, verbose_name="last login"),
                ),
                ("is_admin", models.BooleanField(blank=True, default=False, null=True)),
                ("is_active", models.BooleanField(blank=True, default=True, null=True)),
                ("is_staff", models.BooleanField(blank=True, default=False, null=True)),
                (
                    "is_superuser",
                    models.BooleanField(blank=True, default=False, null=True),
                ),
                ("full_name", models.CharField(blank=True, max_length=30, null=True)),
                ("register_number", models.IntegerField(blank=True, null=True)),
                ("roll_number", models.CharField(blank=True, max_length=3, null=True)),
                (
                    "role",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("admin", "admin"),
                            ("teacher", "teacher"),
                            ("student", "student"),
                        ],
                        default="admin",
                        max_length=30,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]