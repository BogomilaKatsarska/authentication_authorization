from django.contrib.auth.models import User
from django.db import models


# class AppUser(User):
#     def has_email(self):
#         return self.email or False
#     class Meta:
#         proxy = True


class Profile(models.Model):
    first_name = models.CharField(
        max_length=35,
    )
    last_name = models.CharField(
        max_length=35,
    )
    age = models.PositiveIntegerField()
    user = models.OneToOneField(
        User,
        primary_key=True,
        on_delete=models.CASCADE,
    )