from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings
from django.contrib.auth.models import User

class Venue(models.Model):
    locations = [
        ('Edinburgh', 'Edinburgh'),
        ('Glasgow', 'Glasgow'),
        ('other', 'other'),
        ('unknown', 'unknown')
    ]

    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    location = models.CharField(max_length=250, choices=locations, default='Edinburgh')
    submitted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    
    event_types = [
        ('gig', 'gig'),
        ('club', 'club'),
        ('other', 'other'),
        ('unknown', 'unknown'),
    ]

    statuses = [
        ('unknown', 'unknown'),
        ('tickets on sale','tickets on sale'),
        ('just announced', 'just announced'),
        ('sold out', 'sold out'),
        ('cancelled', 'cancelled'),
        ('postponed', 'postponed'),
        ('rescheduled', 'rescheduled'),
        ('change of venue', 'change of venue'),
    ]
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='events_submitted',
        on_delete=models.CASCADE,
        )
    event_type =  models.CharField(max_length=50, choices=event_types, default='gig')
    headline_act = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    venue = models.ForeignKey(
        Venue,
        on_delete=models.CASCADE,
        related_name='events',
        ) 
    date = models.DateField()
    ticket_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=50, choices=statuses, default='unknown')
    promoter = models.CharField(max_length=250, null=True, blank=True)
    submitted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['date']
        indexes = [
            models.Index(fields=['date']),
        ]

    def create_slug(self):
        return slugify(self.headline_act + '-' + self.venue.name + '-' + str(self.date))

    def __str__(self):
        return self.headline_act
        
    def get_absolute_url(self):
        return reverse('event_page', args=[self.slug])
    
    def update_event_url(self):
        return reverse('update_event', args=[self.slug])
    
    def remove_event_url(self):
        return reverse('remove_event', args=[self.slug])
    
    def ticket_price_text(self):
        if self.ticket_price == 0:
            text = 'Free'
        elif self.ticket_price == None:
            text = 'unknown'
        else:
            text = None
        return text
    
    def text_date(self):
        date = self.date
        def suffix(d):
            return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')
        return date.strftime('%a {S} %B').replace('{S}', str(date.day) + suffix(date.day))


    def fri_or_sat(self):
        if self.date.weekday() in [4,5]:
            return True
        else:
            return False