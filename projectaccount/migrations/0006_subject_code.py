# Generated by Django 4.2.6 on 2024-01-10 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectaccount', '0005_rename_passwords_account_copy_pass'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='code',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
