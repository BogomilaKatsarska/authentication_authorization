# from django.http import HttpResponse
#
#
# def allowed_groups(groups=None):
#     if groups is None:
#         groups = []
#
#     def decorator(view_func):
#         def wrapper(request, *args, **kwargs):
#             if not request.user.is_authenticated:
#                 return HttpResponse('Not authenticated')
#             if request.user.is_superuser or not groups:
#                 return view_func(request, *args, **kwargs)
#             user_groups = request.user.groups.filter(name__in=groups)
#
#             if not user_groups:
#                 return HttpResponse('Not in any of the required groups')
#
#             return view_func(request, *args, **kwargs)
#
#         return wrapper
#     print(groups)
#     if callable(groups):
#         func = groups
#         groups = []
#         return decorator(func)
#     return decorator()
