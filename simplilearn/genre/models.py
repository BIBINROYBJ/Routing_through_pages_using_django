from django.db import models

# Create your models here.
class Collection(models.Model):
    collection_name = models.CharField(max_length=100) # I will encounter error in this Collection table or class
    description = models.CharField(max_length=500)
    collcover = models.CharField(max_length=1000)

    def __str__(self):
        return self.collection_name

class Piece(models.Model):
    collection = models.ForeignKey(Collection, on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    typ = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    year = models.IntegerField(4)
    piececover = models.CharField(max_length=1000)


    def __str__(self):
        return self.title