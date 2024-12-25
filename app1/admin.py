from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Student

@admin.register(Student)
class StudentAdmin(UserAdmin):
    # Display fields in the admin list view
    list_display = ('student_id', 'full_names', 'surname', 'email', 'gender', 'date_of_birth', 'mobile_number', 'is_active')

    # Fields to search by
    search_fields = ('student_id', 'full_names', 'surname', 'email', 'mobile_number')

    # Fields for filtering
    list_filter = ('gender', 'is_active', 'is_staff', 'is_superuser')

    # Fieldsets for the detailed view
    fieldsets = (
        (None, {'fields': ('student_id', 'username', 'password')}),
        ('Personal Info', {'fields': ('full_names', 'surname', 'gender', 'date_of_birth', 'email', 'mobile_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Fields for creating/editing students in the admin interface
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_names', 'surname', 'gender', 'date_of_birth', 'email', 'mobile_number', 'password1', 'password2'),
        }),
    )

    # Sorting
    ordering = ('student_id',)
