from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_event, name='submit_event'),
    path('event/<slug:slug>/', views.event_page, name='event_page'),
    path('add_venue/', views.add_venue, name='add_venue'),
    path('event/update/<slug:slug>/', views.update_event, name='update_event'),
    path('event/remove/<slug:slug>/', views.remove_event, name='remove_event'),
    path('my_events/', views.my_events, name='my_events'),
]