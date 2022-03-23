from django.contrib import admin
from .models import Election, Type

# Register your models here.

admin.site.register(Election)

admin.site.register(Type)