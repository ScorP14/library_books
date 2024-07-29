from django.db import models

from django.contrib.auth.models import User


class Users(models.Model):
    pass


class Books(models.Model):
    autor = models.ForeignKey('Users')