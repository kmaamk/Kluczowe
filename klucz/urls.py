from django.conf.urls import url
from django.contrib.auth.views import login
from . import views



app_name="klucz"
urlpatterns =[
    url(r'^$', views.wybierz_kluczowe, name='wybierz_kluczowe'),
    url(r'^login/$', login, {'template_name': 'login2.html'}),
    url(r'potwierdzenie', views.potwierdzenie, name='potwierdzenie'),
    url(r'^error/$', login, {'template_name': 'login_error.html'}),

]