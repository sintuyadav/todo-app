from django import forms 
 
from .models import Mytodo

class todo(forms.ModelForm):
    class Meta:
        model = Mytodo
        fields = ('task','status',)
        
    

