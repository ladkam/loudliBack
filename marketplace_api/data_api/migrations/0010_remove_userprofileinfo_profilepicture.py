# Generated by Django 3.0.3 on 2020-05-21 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_api', '0009_auto_20200407_0706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='profilePicture',
        ),
    ]
