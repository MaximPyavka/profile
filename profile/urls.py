from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^sign_up$', views.sign_up, name='sign_up'),
    url(r'^log_out$', views.log_out, name='log_out'),
    url(r'^log_in$', views.log_in, name='log_in'),
    url(r'^edit$', views.edit_profile, name='edit_profile'),
    url(r'^profile$', views.profile, name='profile'),
]
