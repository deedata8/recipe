from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#cnvention for converting strings to human readable text
from django.utils.translation import gettext as _
from core import models

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    #added a 'name' field
    list_display = ['email', 'name']
    #define sections in the change and create page, each brackets is a section (add a comma at end if only one field)
    #4 sections added, Sections no title, Personal Info, Permissions, Important dates
    fieldsets = (
        (None, {
            'fields': ( 'email', 'password'),
        }),
        (_('Personal Info'), {
            'fields': ('name',
            ),
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'
            ),
        }),
        (_('Important Dates'), {
            'fields': ('last_login',
            ),
        }),
    )

    #customize to include email, pw and pw2
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


# Register the models to the admin page
admin.site.register(models.User, UserAdmin)