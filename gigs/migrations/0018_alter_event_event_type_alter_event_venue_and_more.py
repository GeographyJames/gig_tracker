# Generated by Django 4.2.1 on 2023-05-26 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gigs', '0017_alter_event_venue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('gig', 'gig'), ('club', 'club'), ('other', 'other'), ('unknown', 'unknown')], default='gig', max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='gigs.venue'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='location',
            field=models.CharField(choices=[('Edinburgh', 'Edinburgh'), ('Glasgow', 'Glasgow'), ('other', 'other')], default='Edinburgh', max_length=250),
        ),
    ]
