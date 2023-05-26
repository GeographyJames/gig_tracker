# Generated by Django 4.2.1 on 2023-05-26 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gigs', '0007_remove_event_new_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='sold_out',
        ),
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('sold out', 'sold out'), ('cancelled', 'cancelled'), ('postponed', 'postponed'), ('tickets available', 'tickets available'), ('announced', 'announced')], default='tickets_available', max_length=50),
        ),
    ]
