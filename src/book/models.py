from django.db import models


class Genres(modela.Model):
    title = model.CharField()



class Books(models.Model):
    title = models.CharField()
    autor = models.ForeignKey()
    year = models.IntegerField()

    genre = models.ManyToManyField()
    cover = models.ImageField()
