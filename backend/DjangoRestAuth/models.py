from django.db import models
"""
Here I have defined an example class 'Mods'. Once the client is authenticated, it can request objects of 'Mods' class
and display it back on the client side.
"""


class Mods(models.Model):
    name = models.CharField(max_length=250)
    version = models.CharField(max_length=70)

    def __str__(self):
        return self.name + ' ' + self.version
