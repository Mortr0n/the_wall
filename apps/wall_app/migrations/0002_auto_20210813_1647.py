# Generated by Django 2.2 on 2021-08-13 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration_app', '0002_auto_20210812_1752'),
        ('wall_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]
