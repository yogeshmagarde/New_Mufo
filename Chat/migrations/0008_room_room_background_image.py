# Generated by Django 4.2.2 on 2023-09-07 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0007_chatmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_background_Image',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
