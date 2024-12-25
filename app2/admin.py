from django.contrib import admin
from .models import Staff

class StaffAdmin(admin.ModelAdmin):
    list_display = ('full_names', 'surname', 'gender', 'date_of_birth', 'email', 'mobile_number', 'password')
    search_fields = ('full_names', 'email', 'mobile_number')
    list_filter = ('gender', 'date_of_birth')
    readonly_fields = ('username', 'password')

admin.site.register(Staff, StaffAdmin)
