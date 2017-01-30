
from django.conf.urls import url

from novaposhta import views


urlpatterns = [

    url(r'^autocomplete', views.autocomplete, name='autocomplete')

]
