# Generated by Django 4.1.7 on 2023-04-24 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0062_alter_notmoderatedtournament_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='current_rank',
            field=models.CharField(blank=True, default='0k', max_length=3, null=True, verbose_name='GoLevel'),
        ),
        migrations.AlterField(
            model_name='player',
            name='current_rating',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Rating'),
        ),
    ]
