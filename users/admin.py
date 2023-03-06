from django.contrib import admin
from users.models import Account
from notes.models import Note
from .forms import UserAdminCreationForm,UserAdminChangeForm
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib.auth import get_user_model
User = get_user_model()
# Register your models here.

# class UserAdmin(admin.ModelAdmin):
#     search_fields = ['email']
#     form = UserAdminChangeForm # edit form
#     add_form = UserAdminCreationForm # creation form
#     class Meta:
#         model = User

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['email', 'is_admin']
    list_filter = ['is_admin']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': (['username','first_name','second_name'])}),
        ('Permissions', {'fields': ('is_admin','is_active','is_staff','is_superuser')}),
    )

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()




admin.site.register(User,UserAdmin)
#admin.site.register(Account)
admin.site.register(Note)