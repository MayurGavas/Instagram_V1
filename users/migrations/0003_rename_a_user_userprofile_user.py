# Generated by Django 5.0.3 on 2024-03-12 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_user_userprofile_a_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='a_user',
            new_name='user',
        ),
    ]
