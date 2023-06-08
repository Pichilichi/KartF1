from django.forms import ModelForm,DateInput
from .models import Booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        exclude = ['user', 'racers']
        widgets = {
            'raceDay' : DateInput(attrs={'type':'date'})
        }