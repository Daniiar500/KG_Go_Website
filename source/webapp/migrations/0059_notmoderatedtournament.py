# Generated by Django 4.1.7 on 2023-04-21 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0058_news_video_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotModeratedTournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Tournament name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date of upload')),
                ('uploaded_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='Uploaded by')),
            ],
            options={
                'verbose_name': 'TournamentForModeration',
                'verbose_name_plural': 'TournamentsForModeration',
                'db_table': 'moderation',
            },
        ),
    ]
