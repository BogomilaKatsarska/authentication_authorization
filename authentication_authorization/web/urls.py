from django.urls import path
from authentication_authorization.web.views import ProfileView, UsersListView
from authentication_authorization.web.views import index, create_user_and_login, permission_debug, show_profile

urlpatterns = (
    path('', index, name='index'),
    path('create/', create_user_and_login, name='create'),
    path('debug/', permission_debug, name='debug'),
    path('profile/1/', show_profile, name='show profile'),
    path('profile/2/', ProfileView.as_view(), name='profile view'),
    path('user-list/', UsersListView.as_view(), name='list of users'),
)
