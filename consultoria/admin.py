from django.contrib import admin
from .models import Post, Service, Contact
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

admin.site.register(Post)
admin.site.register(Service)
admin.site.register(Contact)
