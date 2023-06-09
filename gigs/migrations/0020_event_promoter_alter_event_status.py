# Generated by Django 4.2.1 on 2023-06-02 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gigs', '0019_alter_venue_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='promoter',
            field=models.CharField(default='unknown', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('unknown', 'unknown'), ('tickets on sale', 'tickets on sale'), ('just announced', 'just announced'), ('sold out', 'sold out'), ('cancelled', 'cancelled'), ('postponed', 'postponed'), ('rescheduled', 'rescheduled'), ('change of venue', 'change of venue')], default='unknown', max_length=50),
        ),
    ]
