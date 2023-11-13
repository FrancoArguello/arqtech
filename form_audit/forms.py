from django import forms

from form_audit.models import Audit




class FormularioAudit(forms.ModelForm):
    class Meta:
        model = Audit
        fields = '__all__'
        widgets ={}
        

class SearchForm(forms.Form):
    pais = forms.ChoiceField(choices=Audit.pais_choices)
    delegacion = forms.ChoiceField(choices=Audit.delegacion_choices)
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))



