# Generated by Django 3.0.3 on 2020-04-01 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_api', '0005_episodeimported'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episodestat',
            name='episode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_api.EpisodeImported'),
        ),
    ]
