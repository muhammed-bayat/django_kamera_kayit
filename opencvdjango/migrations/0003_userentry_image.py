# Generated by Django 3.2.9 on 2021-11-30 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opencvdjango', '0002_userentry_video_src'),
    ]

    operations = [
        migrations.AddField(
            model_name='userentry',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
