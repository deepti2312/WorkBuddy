from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .models import User


class UserAdmin(BaseUserAdmin):
    
    list_display = ['email', 'first_name', 'last_name', 'is_staff']
    list_filter = ('email',)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    (
                        'email',
                        'first_name',
                        'last_name',
                        'is_staff',
                        'phone',
                        'github_url',
                        'linkedin_url',
                        'notice_period',
                        'groups',
                        'user_permissions',
                    )
                ),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
            },
        ),
    )
    ordering = ('email',)


admin.site.register(User, UserAdmin)
