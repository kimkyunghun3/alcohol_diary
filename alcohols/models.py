from django.db import models

from diaries.models import Diary
from utils.django.models import TimeStampedModel


class AlcoholType(TimeStampedModel):
    alcohol_name = models.CharField('술종류', max_length=100, choices=(
        (1, ("Soju")),
        (2, ("Bear")),
        (3, ("Makgeolli")),
        (4, ("liquor")),
        (5, ("Wine")),
        (6, ("Null"))), default=6
                                    )

    def __str__(self):
        return f'{self.alcohol_name}'


class Alcohol(TimeStampedModel):
    Alcohol_type = models.ForeignKey(AlcoholType, on_delete=models.CASCADE, null=True, related_name='alcohol',choices=(
        # (1, ("Soju")),
        # (2, ("Bear")),
        # (3, ("Makgeolli")),
        # (4, ("liquor")),
        # (5, ("Wine")),
        # (6, ("Null"))), default=6)
    name = models.CharField('술이름', max_length=100)


class AlcoholRecord(TimeStampedModel):
    bottles = models.FloatField(null=True)
    glasses = models.FloatField(null=True)
    alcohol_records = models.ForeignKey(Alcohol, on_delete=models.CASCADE, null=True, related_name='alcohol_records')
    diary = models.ForeignKey(Diary, related_name="alcohol_records", on_delete=models.CASCADE, null=True)
