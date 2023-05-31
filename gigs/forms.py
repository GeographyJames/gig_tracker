from django import forms
from .models import Event, Venue

class SubmitEvent(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['headline_act', 'venue', 'event_type', 'date', 'status', 'ticket_price']

    def __init__(self, *args, **kwargs):
        super(SubmitEvent, self).__init__(*args, **kwargs)

        self.fields['headline_act'].widget.attrs['class'] = 'form-control'
        self.fields['headline_act'].widget.attrs['placeholder'] = 'Event name or headline act'

        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'}) # For some reason Django seems to default date fields to text input so we so we set the type to date here.
        self.fields['date'].widget.attrs['class'] = 'form-control'

        self.fields['event_type'].widget.attrs['class'] = 'form-select'

        self.fields['status'].widget.attrs['class'] = 'form-select'

        self.fields['venue'].widget.attrs['class'] = 'form-select'
        self.fields['venue'].empty_label='Select venue'

        self.fields['ticket_price'].widget.attrs['class'] = 'form-select'
        self.fields['ticket_price'].label = 'Ticket price face value (excluding booking fee)'

class AddVenue(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'location']

    def __init__(self, *args, **kwargs):
        super(AddVenue, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Venue name'
        self.fields['name'].label = ''

        self.fields['location'].widget.attrs['class'] = 'form-select'
        self.fields['location'].label = ''

