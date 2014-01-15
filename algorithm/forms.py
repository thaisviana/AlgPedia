from algorithm.models import Classification
from django import forms


class FiltersAlgorithm(forms.Form):
    search = forms.CharField()
    classifications = forms.ModelChoiceField(queryset=Classification.objects.all(), empty_label="All")