from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='landing')
     url(r'^upload/$', views.new_project, name='newPro'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
]