# Generated by Django 3.0.3 on 2020-04-01 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_api', '0002_podcast_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='durationMax',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='durationMin',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='editor',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='listenNotesId',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='thumbnail',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='podcast',
            name='type',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
