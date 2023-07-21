from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from account.models.user import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_per_page = 200
    save_on_top =True
    list_display = (
        'phone_number',
        'email',
        'username',
        'first_name',
        'last_name',

    )
    search_fields = ['email','phone_number']
    list_filter = (
        'created',
        'modified'
    )
    # autocomplete_fields = (
    #     "posts",
    #     "replies",
    # )
    fieldsets = (
        (_("Information"),{
        "fields":(
            'first_name',
            'last_name',
            'username',
            
        )
    }),
        (_("create account"), {
            "fields":(
                'email',
                'phone_number',
                'password',
            )
        }),
        
    )