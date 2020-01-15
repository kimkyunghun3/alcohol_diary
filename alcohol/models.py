from django.db import models


class Alcohol(models.Model):
    Alcohol_name = models.CharField('술이름', max_length=100)
    volume = models.IntegerField()

    def __str__(self):
        return f'{self.Alcohol_name}, {self.volume}'
