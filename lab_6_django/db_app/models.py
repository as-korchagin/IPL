from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=1023)
    description = models.TextField(default='')
    birth_date = models.DateField(default=None, null=True)
    death_date = models.DateField(default=None, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Genre(models.Model):
    name = models.CharField(max_length=1023)
    description = models.TextField(default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Book(models.Model):
    name = models.CharField(max_length=1023)
    description = models.TextField(default='')
    author = models.ManyToManyField(Author)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
