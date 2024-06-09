from django.db import models
from musician.models import Musician
class Albums( models.Model ):
    name = models.CharField(max_length=100)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateTimeField()
    RATING = [('1','One'),
              ('2','Two'),
              ('3','Three'),
              ('4','Four'),
              ('5','Five'),
              ]
    rating = models.CharField(choices=RATING, max_length=50)

