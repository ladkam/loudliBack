# Generated by Django 3.0.3 on 2020-04-01 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='pub_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
