# Generated by Django 3.0.3 on 2020-05-25 17:03

import data_api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_api', '0010_remove_userprofileinfo_profilepicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='podcastPicture',
            field=models.ImageField(blank=True, null=True, upload_to=data_api.models.scramble_uploaded_filename),
        ),
    ]
