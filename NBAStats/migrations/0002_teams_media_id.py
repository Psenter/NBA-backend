# Generated by Django 4.2.4 on 2023-08-25 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NBAStats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='media_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='NBAStats.media'),
        ),
    ]