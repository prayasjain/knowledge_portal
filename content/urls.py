from django.conf.urls import patterns, url
from content import views

urlpatterns = patterns('',url(r'^$',views.index,name="index"),
                       url(r'^post/',views.post,name="publish"),)