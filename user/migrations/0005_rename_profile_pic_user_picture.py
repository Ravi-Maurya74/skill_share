# Generated by Django 5.0.4 on 2024-05-04 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_remove_user_firebase_uid_user_email_user_uid"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="profile_pic",
            new_name="picture",
        ),
    ]
