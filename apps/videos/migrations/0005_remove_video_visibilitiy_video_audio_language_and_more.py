# Generated by Django 5.1.4 on 2024-12-30 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_delete_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='visibilitiy',
        ),
        migrations.AddField(
            model_name='video',
            name='audio_language',
            field=models.CharField(choices=[('en', 'English'), ('ru', 'Russian'), ('uz', 'Uzbek')], default='en', max_length=2),
        ),
        migrations.AddField(
            model_name='video',
            name='comments_enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='video',
            name='is_age_restricted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='video',
            name='is_premium',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='video',
            name='license',
            field=models.CharField(choices=[('s', 'Standart YouTube License'), ('c', 'Creative Commons')], default='s', max_length=20),
        ),
        migrations.AddField(
            model_name='video',
            name='related_videos',
            field=models.ManyToManyField(blank=True, related_name='related_to', to='videos.video'),
        ),
        migrations.AddField(
            model_name='video',
            name='video_file',
            field=models.FileField(default=1, upload_to='video/file/%Y/%m/%d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='visibility',
            field=models.CharField(choices=[('Public', 'Public'), ('Private', 'Private'), ('Unlisted', 'Unlisted')], default='Public', max_length=10),
        ),
    ]
