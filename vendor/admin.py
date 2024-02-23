from django.contrib import admin
from django import forms
from .models import Vendor


class VendorAdmin(admin.ModelAdmin):
    list_display = []
    readonly_fields = []

admin.site.register(Vendor, VendorAdmin)

