# Generated by Django 3.2.9 on 2021-12-12 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_auto_20211211_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='avatar',
            field=models.ImageField(upload_to='avatares'),
        ),
    ]