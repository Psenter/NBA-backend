# Generated by Django 4.2.4 on 2023-08-16 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NBAStats', '0006_players_jersey_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='weight',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
