from django.db import models


class Mods(models.Model):
    name = models.CharField(max_length=250)
    version = models.CharField(max_length=70)

    def __str__(self):
        return self.name + ' ' + self.version
