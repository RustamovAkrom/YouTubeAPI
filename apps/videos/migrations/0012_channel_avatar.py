# Generated by Django 5.1.4 on 2025-01-02 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0011_alter_notification_notification_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='channel/avatar/%Y/%m/%d'),
        ),
    ]