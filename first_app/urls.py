from django.conf.urls import url
from first_app import views

app_name = 'first_app'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^locations/$', views.locations, name='locations'),
    url(r'^formpage/$', views.form_name_view, name='form_name')
]
