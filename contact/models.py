from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=200, null=False)
    email = models.EmailField(null=False, blank=False)
    message = models.TextField(null=False)

    def __str__(self):
        return self.name
