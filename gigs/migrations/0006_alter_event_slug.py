# Generated by Django 4.2.1 on 2023-05-26 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gigs', '0005_alter_event_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]
