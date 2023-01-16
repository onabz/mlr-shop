from django.db import models


class DollType(models.Model):
    """ A model to manage doll categories """

    name = models.CharField(max_length=25, null=False, blank=False)

    def __str__(self):
        return self.name
