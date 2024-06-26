from django.db import models

class Book(models.Model):
    pages = models.IntegerField()
    release = models.DateTimeField()
    title = models.CharField(max_length=255)
    writtenBy = models.ManyToManyField('Author')
    locatedIn = models.ForeignKey('Library', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id)

class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)

class Library(models.Model):
    address = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)




