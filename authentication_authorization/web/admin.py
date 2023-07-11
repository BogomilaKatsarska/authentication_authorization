from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from authentication_authorization.auth_app.views import SignUpForm

UserModel = get_user_model()

@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    ordering = ('email,')
    list_display = ['email', 'date_joined', 'last_login']
    list_filter = ()
    add_form = SignUpForm
