from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views import generic as views
from django.shortcuts import render

from django.contrib.auth.models import User

from authentication_authorization.web.decorators import allowed_groups


@allowed_groups(groups=['Users'])
def index(request):
    print(
        ## with 'alt' you can mark on more than one place (via using mouse)
        authenticate(username='donchominkov', password='d0n4omink0v'),
        authenticate(username='hristo-pc', password='123'),
        authenticate(username='minkov', password='doncho123!@'),
    )
    # new_user = User.objects.create_user(
    #     username='donchominkov',
    #     password='d0n40mink0v',
    #     first_name='doncho',
    # )
    #is_authenticated always returns True[because you are either AnonymousUser or authenticated user].
    print(request.user)
    user_message = '' if request.user.is_authenticated else 'not '
    return HttpResponse(f' The user is {user_message}authenticated.')

#User.objects.create_user()
#print(user.has_perms())


def create_user_and_login(request):
    print(request.user)
    user = User.objects.create_user(
        username='Pesho',
        password='Goshov123!@',
    )
    login(request, user)
    print(request.user)
    return HttpResponse('It works')


def permission_debug(request):
    usernames = {'donchominkov', 'hristo-pc', 'minkov'}
    users = User.objects.filter(username__in=usernames)
    permissions_to_check = ['auth.add_user', 'auth.change_user', 'auth.delete_user', 'auth.view_user']
    for user in users:
        print('-' * 30)
        print(user)
        #Below: user must have all of the permissions from 'permissions_to_check'
        print(user.has_perms(permissions_to_check))
        #Below: user must have any permission from 'permissions_to_check'
        for perm in permissions_to_check:
            print(user.has_perm(perm))
        print('-' * 30)

    return HttpResponse('It works')


#Function-based views
@login_required(login_url='/login')
def show_profile(request):
    return HttpResponse(f'You are {request.user.username}')


#CBV
class ProfileView(LoginRequiredMixin, views.View):
    def get(self, request):
        return HttpResponse(f'You are {request.user.username}')
