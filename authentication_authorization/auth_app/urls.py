from django.contrib.auth.views import LoginView
from django.urls import path

from authentication_authorization.auth_app.views import SignUpView

urlpatterns = (
    path('sign-up/', SignUpView.as_view(), name='sign up'),
    path('sign-in/', LoginView.as_view(), name='sign in'),
    # path('sign-in/', sign_in, name='sign in'),
)