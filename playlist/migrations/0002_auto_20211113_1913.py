# Generated by Django 2.2.1 on 2021-11-13 13:13

from django.db import migrations, models
import playlist.models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default='My Playlist', null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=playlist.models.upload_location)),
                ('listenings', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
