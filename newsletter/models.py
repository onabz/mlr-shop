from django.db import models


class Newsletter(models.Model):
    email = models.EmailField(null=False, blank=False)

    def __str__(self):
        return self.email


class SendMessage(models.Model):
    title = models.CharField(max_length=100, null=False)
    message = models.TextField(null=False)

    def __str__(self):
        return self.title
