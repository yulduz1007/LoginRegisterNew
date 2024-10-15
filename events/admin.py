from django.contrib import admin
from django.contrib.admin import AdminSite

from events.models import Event, Product


# Register your models here.


class EventSiteAdmin(AdminSite):
    site_header = 'Event Admin'
    site_title = 'Event admin title'
    index_title = 'Welcome to Event Admin'


event_admin_site = EventSiteAdmin(name='Event Admin11')


event_admin_site.register(Event)
event_admin_site.register(Product)



