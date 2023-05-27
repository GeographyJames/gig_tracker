# Generated by Django 4.2.1 on 2023-05-25 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('submitted', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('gig', 'gig'), ('club', 'club')], max_length=50)),
                ('headline_act', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('date', models.DateField()),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sold_out', models.BooleanField()),
                ('submitted', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='gigs.venue')),
            ],
            options={
                'ordering': ['-date'],
                'indexes': [models.Index(fields=['-date'], name='gigs_event_date_f25d1a_idx')],
            },
        ),
    ]