# Generated by Django 4.2.1 on 2023-06-02 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gigs', '0021_alter_event_promoter'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='events_submitted', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
