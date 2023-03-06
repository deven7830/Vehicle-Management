from django import forms
from . import models


class VehicleForm(forms.ModelForm):
    class Meta:
        model = models.VehicleModel
        fields = '__all__'

