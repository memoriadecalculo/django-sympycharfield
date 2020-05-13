from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.SympyCharFieldTestList.as_view(), name='formulas'),
    url(r'^(?P<pk>[A-Z0-9-]+)/$', views.SympyCharFieldTest.as_view(), name='formulas'),
]