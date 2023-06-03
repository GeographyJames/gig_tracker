from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Event, Venue
from .forms import SubmitEvent, AddVenue
from django.contrib import messages
from django.utils.text import slugify
import pandas as pd
import datetime
from django.contrib.auth.decorators import login_required


def home(request):

    date_range = pd.date_range(
        start = datetime.date.today().strftime('%Y-%m'),
        end = Event.objects.latest('date').date.strftime('%Y-%m'),
        freq='MS')

    events_by_month = {}
    for date in date_range:
        events = Event.objects.filter(date__year=date.year, date__month=date.month)
        events_by_month[date.strftime("%b %Y")] = events

    return render(request, 'events/home.html', {
        'events_by_month': events_by_month,
        })

@login_required
def submit_event(request):
    if request.method != 'POST':
        form = SubmitEvent()

    if request.method == 'POST':
        form = SubmitEvent(data=request.POST)
        if form.is_valid():
            print(type(form.cleaned_data['ticket_price']), form.cleaned_data['ticket_price'])
            event = form.save(commit=False)
            event.user = request.user
            event.slug = event.create_slug()
            existing_event = Event.objects.filter(
                date=event.date,
                slug=event.slug
                )
            if existing_event:
                messages.warning(
                    request,
                    f"There is already an event with {event.headline_act} at {event.venue} on {event.text_date()} in the database.")
            else:

                event.save()
                messages.success(
                    request,
                    f"<strong>{event.headline_act}</strong> at <strong>{event.venue}</strong> on <strong>{event.text_date()}</strong> added to database.")
                return redirect('home')

    return render(request, 'events/submit_event.html', {'form': form})

def event_page(request, slug):
    event = get_object_or_404(
        Event,
        slug=slug
        )

    return render(request, 'events/event_page.html', {'event': event})

@login_required
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
                messages.warning(
                    request,
                    f"You tried to add <strong>{venue.name}</strong> but there is already a venue called <strong>{existing_venue[0].name}</strong> in the database. These names are too similar."
                    )
            else:
                venue.save()
                messages.success(request, f"<strong>{venue.name}</strong> added to database.")
                return redirect('submit_event')

    return render(request, 'events/add_venue.html', {'form': form})

@login_required
def update_event(request, slug):
    event = get_object_or_404(
    Event,
    slug=slug
    )
    return render(request, 'events/update_event.html', {})

@login_required
def remove_event(request, slug):
    event = get_object_or_404(Event, slug=slug)
    if request.user == event.user:
        event.delete()
        messages.success(
            request,
            f"<strong>{event.headline_act}</strong> at <strong>{event.venue}</strong> on <strong>{event.text_date()}</strong> removed from the database."
            )
    else: messages.warning(request, 'Only the user that submitted the event may remove it.')
    return redirect ('home')

@login_required
def my_events(request):
    my_events = Event.objects.filter(user=request.user)    
    return render(request, 'events/my_events.html', {'events': my_events})