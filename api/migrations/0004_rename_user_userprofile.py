# Generated by Django 4.2.3 on 2023-07-19 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_resume_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserProfile',
        ),
    ]
