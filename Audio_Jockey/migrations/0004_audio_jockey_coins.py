# Generated by Django 4.2.1 on 2023-07-26 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Audio_Jockey', '0003_audio_jockey_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio_jockey',
            name='coins',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
