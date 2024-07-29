from django.db import models


class Books(models.Model):
    autor = models.ForeignKey("Users")
