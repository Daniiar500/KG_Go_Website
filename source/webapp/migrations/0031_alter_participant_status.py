# Generated by Django 4.1.7 on 2023-03-21 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0030_participant_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='status',
            field=models.CharField(choices=[('Confirmed', 'Confirmed'), ('No Confirmed ', 'No Confirmed')], default='Confirmed', max_length=50, verbose_name='Статус'),
        ),
    ]
