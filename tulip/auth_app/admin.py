from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import UserCreationForm

# Overridden Useradmin to show additional fields.

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    add_fieldsets = (
        *UserAdmin.fieldsets, 
        (                      
            None,  
            {
                'fields': (
                    'user_role',
                ),
            },
        ),
    )

admin.site.register(User,CustomUserAdmin)


