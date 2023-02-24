from django.db import models


class Saying(models.Model):
    """ A model to manage random sayings on the home page """

    message = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.message
