# Generated by Django 5.1.4 on 2024-12-30 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_remove_channel_views_count'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
