from django.forms import Textarea, ModelForm


class AlgorithmForm(ModelForm):
    class Meta:
        from algorithm.models import Algorithm
        model = Algorithm
        fields = '__all__'
        widgets = {
			'description': Textarea(attrs={'cols': 240, 'rows': 10}),
		}
	
	# def save(self, commit=True):
	# 	algorithm = super(AlgorithmForm, self).save(commit=False)
	# 	if commit:
	# 		algorithm.save()
	# 	return algorithm
