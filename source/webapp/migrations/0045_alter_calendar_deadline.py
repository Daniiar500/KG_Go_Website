# Generated by Django 4.1.7 on 2023-03-30 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0044_partner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='deadline',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания регистрации'),
        ),
    ]