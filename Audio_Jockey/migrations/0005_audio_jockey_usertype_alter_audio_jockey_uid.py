# Generated by Django 4.2.2 on 2023-08-27 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Audio_Jockey', '0004_audio_jockey_coins'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio_jockey',
            name='usertype',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='audio_jockey',
            name='uid',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
