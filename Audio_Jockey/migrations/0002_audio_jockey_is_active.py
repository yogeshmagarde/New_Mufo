# Generated by Django 4.0.1 on 2023-06-29 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Audio_Jockey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio_jockey',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
