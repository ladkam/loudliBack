# Generated by Django 3.0.3 on 2020-05-25 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_api', '0011_auto_20200525_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='nb_episodes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
