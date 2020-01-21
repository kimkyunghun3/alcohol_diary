from django.db import models

from diaries.models import Diary
from utils.django.models import TimeStampedModel


class AlcoholType(TimeStampedModel):
    alcohol_name = models.CharField('술종류', max_length=100)

    def __str__(self):
        return f'{self.Alcohol_name}'


class Alcohol(TimeStampedModel):
    Alcohol_type = models.ForeignKey(AlcoholType, on_delete=models.CASCADE, null=True)
    name = models.CharField('술이름', max_length=100)


class AlcoholRecord(TimeStampedModel):
    bottles = models.FloatField()
    glasses = models.FloatField()
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE, null=True)
