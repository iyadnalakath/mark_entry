# Generated by Django 4.2.6 on 2023-10-12 07:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="SeriesExam",
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
                ("name", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(blank=True, max_length=50, null=True)),
                ("register_number", models.IntegerField(blank=True, null=True)),
                ("roll_number", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Questions",
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
                ("question_one", models.IntegerField(blank=True, null=True)),
                (
                    "question_one_co",
                    models.CharField(blank=True, max_length=5, null=True),
                ),
                ("question_two", models.IntegerField(blank=True, null=True)),
                (
                    "question_two_co",
                    models.CharField(blank=True, max_length=5, null=True),
                ),
                ("question_three", models.IntegerField(blank=True, null=True)),
                (
                    "question_three_co",
                    models.CharField(blank=True, max_length=5, null=True),
                ),
                ("question_four", models.IntegerField(blank=True, null=True)),
                (
                    "question_four_co",
                    models.CharField(blank=True, max_length=5, null=True),
                ),
                ("question_five", models.IntegerField(blank=True, null=True)),
                (
                    "question_five_co",
                    models.CharField(blank=True, max_length=5, null=True),
                ),
                ("question_six", models.IntegerField(blank=True, null=True)),
                (
                    "question_six_co",
                    models.CharField(blank=True, max_length=5, null=True),
                ),
                ("question_seven", models.IntegerField(blank=True, null=True)),
                (
                    "question_seven_co",
                    models.CharField(blank=True, max_length=5, null=True),
                ),
                ("question_eight", models.IntegerField(blank=True, null=True)),
                (
                    "question_eight_co",
                    models.CharField(blank=True, max_length=5, null=True),
                ),
                ("question_nine", models.IntegerField(blank=True, null=True)),
                (
                    "question_nine_co",
                    models.CharField(blank=True, max_length=5, null=True),
                ),
                ("question_ten", models.IntegerField(blank=True, null=True)),
                (
                    "question_ten_co",
                    models.CharField(blank=True, max_length=5, null=True),
                ),
                (
                    "exam_name",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="series_exam",
                        to="store.seriesexam",
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="teacher",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
