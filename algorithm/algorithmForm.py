from algorithm.models import Algorithm
from django import forms
from django.forms import Textarea

class AlgorithmForm(forms.ModelForm):
	class Meta:
		model = Algorithm
		fields = ('name','description','classification')
		widgets = {
            'description': Textarea(attrs={'cols': 240, 'rows': 10}),
        }
	
	def save(self, commit=True):
		algorithm = super(AlgorithmForm, self).save(commit=False)
		if commit:
			algorithm.save()
		return algorithm