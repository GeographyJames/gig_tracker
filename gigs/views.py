from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Event, Venue
from .forms import SubmitEvent, AddVenue
from django.contrib import messages
from django.utils.text import slugify
import pandas as pd
import datetime

def suffix(d):
    return 'th' if 11<=d<=13 else {1:'st',2:'nd',3:'rd'}.get(d%10, 'th')

def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

def home(request):

    date_range = pd.date_range(
        start = datetime.date.today().strftime('%Y-%m'),
        end = Event.objects.latest('date').date.strftime('%Y-%m'),
        freq='MS')

    events_by_month = {}
    for date in date_range:
        events = Event.objects.filter(date__year=date.year, date__month=date.month)
        for event in events:
            event.text_date=custom_strftime('%a {S} %B', event.date)
            if event.date.weekday() in [4,5]:
                event.fri_or_sat = True
            else:
                event.fri_or_sat = False

        events_by_month[date.strftime("%b %Y")] = events

    return render(request, 'events/home.html', {'events_by_month': events_by_month})


def submit_event(request):
    if request.method != 'POST':
        form = SubmitEvent()

    if request.method == 'POST':
        form = SubmitEvent(data=request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.slug = event.create_slug()
            existing_event = Event.objects.filter(
                date=event.date,
                slug=event.slug
                )
            if existing_event:
                messages.warning(request, f"There is already an event with {event.headline_act} at {event.venue} on {custom_strftime('%a {S} %B %Y', event.date)} in the database.")
            else:
                event.save()
                messages.success(request, f"<strong>{event.headline_act}</strong> at <strong>{event.venue}</strong> on <strong>{custom_strftime('%a {S} %B %Y', event.date)}</strong> added to database.")
                return redirect('home')

    return render(request, 'events/submit_event.html', {'form': form})

def event_page(request, slug):
    event = get_object_or_404(
        Event,
        slug=slug
        )

    return render (request, 'events/event_page.html', {'event': event})

def add_venue(request):
    if request.method != 'POST':
        form = AddVenue()

    if request.method == 'POST':
        form = AddVenue(data=request.POST)
        if form.is_valid():
            venue = form.save(commit=False)
            venue.slug = slugify(venue.name)
            existing_venue = Venue.objects.filter(slug=venue.slug)
            if existing_venue:
                print(existing_venue)
                messages.warning(request, f"You tried to add <strong>{venue.name}</strong> but there is already a venue called <strong>{existing_venue[0].name}</strong> in the database. These names are too similar.")
            else:
                venue.save()
                messages.success(request, f"<strong>{venue.name}</strong> added to database.")
                return redirect('submit_event')


    return render(request, 'events/add_venue.html', {'form': form})
