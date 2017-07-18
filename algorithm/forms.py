from algorithm.models import Classification, Tag
from django import forms


class FiltersAlgorithm(forms.Form):
    search = forms.CharField()
    classification = forms.ModelChoiceField(queryset=Classification.objects.all(), empty_label="All")


class FiltersClassification(forms.Form):
    search = forms.CharField()


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
