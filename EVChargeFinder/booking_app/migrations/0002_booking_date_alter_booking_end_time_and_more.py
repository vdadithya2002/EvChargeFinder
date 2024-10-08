# Generated by Django 5.1.1 on 2024-10-08 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.TimeField(),
        ),
    ]