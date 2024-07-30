from django.db import models


class Authors(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Имя",
        help_text="Имя автора",
    )


class Genres(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Жанр",
        help_text="Жанр книги",
    )


def user_directory_path(instance):
    return "{0}".format(instance.id)


class Books(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Название книги",
        help_text="Название книги",
    )

    author = models.ManyToManyField(
        "Authors",
        related_name="books",
        verbose_name="Авторы книги",
        help_text="Авторы",
    )

    year = models.PositiveIntegerField(
        verbose_name="Год выхода книги",
        help_text="год выхода книге",
    )

    genre = models.ManyToManyField(
        Genres,
        related_name="books",
        verbose_name="Жанры книги",
        help_text="Жанры",
    )
    cover = models.ImageField(
        upload_to=user_directory_path,
        storage=None,
        max_length=100,
        blank=True,
        null=True,
    )


def create():
    list_author = ['Сашя', 'Маша', 'Даша', 'Каша', 'Петя', ]
    list_genre = ['Мелодрама', 'манга', '18+', "ужасы", "боевик"]
    books = [
        {'title': 'Книга 1', 'author': ['Петя', 'Даша'], 'year': 2027, 'genre': ['18+', "Мелодрама"]},
        {'title': 'Книга 2', 'author': ['Маша', 'Сашя'], 'year': 2021, 'genre': ['манга', "ужасы"]},
        {'title': 'Книга 3', 'author': ['Каша', 'Петя'], 'year': 2025, 'genre': ['боевик', "ужасы"]},
    ]
