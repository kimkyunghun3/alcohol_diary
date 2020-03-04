from django.db import models

from diaries.models import Diary
from utils.django.models import TimeStampedModel

"""
-        (1, ("Soju")),
-        (2, ("Bear")),
-        (3, ("Makgeolli")),
-        (4, ("liquor")),
-        (5, ("Wine")),
-        (6, ("Null"))), default=6
"""

class AlcoholType(TimeStampedModel):
    alcohol_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.alcohol_name}'


class Alcohol(TimeStampedModel):
    alcohol_type = models.ForeignKey(AlcoholType, on_delete=models.CASCADE, null=True, related_name='alcohol_type')
    name = models.CharField('술이름', max_length=100)


class AlcoholRecord(TimeStampedModel):
    bottles = models.FloatField(null=True)
    glasses = models.FloatField(null=True)
    alcohol = models.ForeignKey(Alcohol, on_delete=models.CASCADE, null=True, related_name='alcohol')
    diary = models.ForeignKey(Diary, related_name="alcohol_records", on_delete=models.CASCADE, null=True)
