# Generated by Django 3.2.9 on 2021-12-12 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0006_auto_20211212_1127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avatar',
            old_name='imagen',
            new_name='avatar',
        ),
    ]
