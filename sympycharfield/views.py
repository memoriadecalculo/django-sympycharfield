from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from . import models, forms

# Create your views here.
class SympyCharFieldTest(UpdateView):
    model = models.SympyCharFieldTest
    form_class = forms.SympyCharFieldTest
    success_url = '.'

class SympyCharFieldTestList(ListView):
    model = models.SympyCharFieldTest
