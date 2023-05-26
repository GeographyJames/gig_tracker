from django.db import models
from django.urls import reverse
from django.utils.text import slugify

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
        
    ]

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