from django.db import models
from image.models import Image
from alcohol.models import Alcohol
from utils.django.models import TimeStampedModel


class DailyRecord(TimeStampedModel):
    drunken_type = (
        ("drunken", "3volume"),
        ("So_so", "1volume"),
        ("not_drunken", "0.5volume"),
    )
    hangover_type = (
        ("too_bad", "want_to_die"),
        ("so_so", "need_to_eat"),
        ("great", "nothing"),
    )

    creator = models.ForeignKey(
        "account.User",
        on_delete=models.CASCADE,
        null=True,
        related_name='daily_record'
    )

    comment = models.CharField(max_length=300,null =True)
    alcohol = models.ForeignKey(Alcohol, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True, related_name='daily_record')
    date = models.TimeField(null=True)
    drunken = models.CharField(max_length=50, choices=drunken_type, default="not_drunken")
    hangover = models.CharField(max_length=50, choices=hangover_type, default="great")

    def __str__(self):
        return f'Time Record - {self.creator}'
