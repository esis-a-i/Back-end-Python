from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title of book")

    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(
        max_length=1000, help_text="Enter a brief description of the book", verbose_name="Summary", null=True, blank=True)

    genre = models.ManyToManyField(
        'Genre', help_text="Select a genre for this book")

    class Meta:
        ordering = ['-id']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self)])


class Genre(models.Model):
    name = models.CharField(
        max_length=200, help_text="Enter a book genre", verbose_name="Genre")

    class Meta:
        ordering = ['-id']
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("genre_detail", args=[str(self)])


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="First name")

    last_name = models.CharField(max_length=100, verbose_name="Last name")

    date_of_birth = models.DateField(
        null=True, blank=True, verbose_name="Date of birth")

    date_of_death = models.DateField(
        null=True, blank=True, verbose_name="Date of death")

    class Meta:
        ordering = ['-id']
        verbose_name = 'Author'
        verbose_name_plural = 'Author'

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self)])
