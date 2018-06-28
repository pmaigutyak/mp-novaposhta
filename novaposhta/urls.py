
from django.conf.urls import url

from novaposhta import views


app_name = 'novaposhta'


urlpatterns = [

    url('autocomplete', views.autocomplete, name='autocomplete'),

    url('refresh', views.refresh, name='refresh')

]
