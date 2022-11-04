from django.contrib import admin

# Register your models here.
from .models import MyUser,Address
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



class UserModelAdmin(BaseUserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'name','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ("UserCredentials", {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name','phone')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('',),
            'fields': ('email', 'name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email','name')
    ordering = ('email','id')
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(MyUser, UserModelAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display = ('user','address','place','zipcode','phone')
    list_filter = ('user',)
    search_fields = ('user','address','place','zipcode','phone')
    ordering = ('user','id')
    filter_horizontal = ()



admin.site.register(Address,AddressAdmin)