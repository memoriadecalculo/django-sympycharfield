from .                   import models
from django.forms.models import ModelForm

class SympyCharFieldTest(ModelForm):
    class Meta:
        model = models.SympyCharFieldTest
        fields = ['formula',]
