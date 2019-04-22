from django import forms 
from .models import *
  
class ImagesForm(forms.ModelForm): 
    class Meta: 
        model = Image 
        fields = ['imgName', 'img' ] 