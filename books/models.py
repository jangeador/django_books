from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author_edit', kwargs={'pk': self.pk})


class Book(models.Model):
    name = models.CharField(max_length=200)
    pages = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})
