from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class Mods(models.Model):
    name = models.CharField(max_length=250)
    version = models.CharField(max_length=70)

    def __str__(self):
        return Mods.name + Mods.version


class BlacklistMixin(blacklist):
    token = RefreshToken()
    token.blacklist()
