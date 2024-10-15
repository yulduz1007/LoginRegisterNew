from django.contrib import admin
from django.contrib.auth.models import Group, User

from apps.models import Category

admin.site.site_header = "UMRA Admin"
admin.site.site_title = "UMRA Admin Portal"
admin.site.index_title = "Welcome to UMRA Researcher Portal"

admin.site.register(Category)

admin.site.unregister(Group)
# admin.site.unregister(User)