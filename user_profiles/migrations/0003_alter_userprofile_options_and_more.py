# Generated by Django 4.2.10 on 2024-06-21 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user_profiles", "0002_userprofile_fave_cosplay_userprofile_next_convention"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="userprofile",
            options={},
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="profile_image",
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="updated_at",
        ),
    ]
