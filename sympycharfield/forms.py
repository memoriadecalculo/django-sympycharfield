from django.forms.models import ModelForm
from . import models

class SympyCharFieldTest(ModelForm):
    class Meta:
        model = models.SympyCharFieldTest
        fields = ['formula',]