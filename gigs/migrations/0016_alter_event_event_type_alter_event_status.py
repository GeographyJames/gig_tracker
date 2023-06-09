# Generated by Django 4.2.1 on 2023-05-26 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gigs', '0015_alter_venue_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('gig', 'gig'), ('club', 'club'), ('other', 'other')], default='gig', max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('unknown', 'unknown'), ('tickets on sale', 'tickets on sale'), ('just announced', 'just announced'), ('sold out', 'sold out'), ('cancelled', 'cancelled'), ('postponed', 'postponed')], default='unknown', max_length=50),
        ),
    ]
