from django.contrib import admin

# Register your models here.
from .models import projects,cert
admin.site.register(projects)
admin.site.register(cert)
