from django.conf.urls import  include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import login
admin.autodiscover()

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.haml')),


    # login / logout
    url(r'^accounts/login/$', login, name="login"),
    url(r'^accounts/logout/$', login, name="logout"),

    # admin page
    url(r'^admin/', admin.site.urls)
]
