from django.db import models


class Genres(modela.Model):
    title = model.CharField(
        max_length=50,
        unique=True,
        verbose_name="Жанр",
        help_text="Жанр книги",
    )


def user_directory_path(instance):
    return "{1}".format(instance.id)


class Books(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Название книги",
        help_text="Название книги",
    )

    autor = models.ManyToManyField(
        "Users",
        on_delete=models.SET_NULL,
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
        on_delete=models.SET_NULL,
        related_name="books",
        verbose_name="Жанры книги",
        help_text="Жанры",
    )
    cover = models.ImageField(
        upload_to=user_directory_path,
        storage=None,
        max_length=100,
    )
