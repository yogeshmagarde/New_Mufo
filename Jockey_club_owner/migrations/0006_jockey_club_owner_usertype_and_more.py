# Generated by Django 4.2.2 on 2023-08-27 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jockey_club_owner', '0005_jockey_club_owner_coins'),
    ]

    operations = [
        migrations.AddField(
            model_name='jockey_club_owner',
            name='usertype',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jockey_club_owner',
            name='uid',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]