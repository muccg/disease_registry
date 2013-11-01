from django.conf.urls import patterns
from django.conf.urls import include
from django.contrib import admin

urlpatterns = patterns('',
                       (r"^$", 'dm1.dm1.views.index'))