from django.contrib import admin
from . models import Venue, Event

admin.site.register(Event)
admin.site.register(Venue)