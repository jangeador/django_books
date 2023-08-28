from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("author_edit", kwargs={"pk": self.pk})


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    image_link = models.CharField(max_length=200, blank=True)
    language = models.CharField(max_length=200, blank=True)
    link = models.CharField(max_length=1024, blank=True)
    pages = models.IntegerField()
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_edit", kwargs={"pk": self.pk})
