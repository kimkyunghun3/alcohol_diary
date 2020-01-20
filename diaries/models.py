from django.db import models
from utils.django.models import TimeStampedModel


class Diary(TimeStampedModel):
    drunken_level = (
        ("drunken", "3volume"),
        ("So_so", "1volume"),
        ("not_drunken", "0.5volume"),
    )
    hangover_level = (
        ("too_bad", "want_to_die"),
        ("so_so", "need_to_eat"),
        ("great", "nothing"),
    )
    action_type = (
        ("die", "die"),
        ("good", "good"),
        ("heaven", "heaven"),
    )

    creator = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        related_name='diaries'
    )

    review = models.CharField(max_length=300, null=True)
    date = models.TimeField(null=True)
    drunken_level = models.CharField(max_length=50, choices=drunken_level, default="not_drunken")
    hangover_level = models.CharField(max_length=50, choices=hangover_level, default="great")
    action_type = models.CharField(max_length=50, choices=action_type, )

    def __str__(self):
        return f'Time Record - {self.creator}'
