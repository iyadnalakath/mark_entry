# Generated by Django 4.2.6 on 2023-10-12 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="questions",
            name="student",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="student_name",
                to="store.student",
            ),
        ),
        migrations.AlterField(
            model_name="questions",
            name="exam_name",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="series",
                to="store.seriesexam",
            ),
        ),
        migrations.AlterField(
            model_name="questions",
            name="teacher",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="teacher_name",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
