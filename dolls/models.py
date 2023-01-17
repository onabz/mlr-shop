from django.db import models
from cloudinary.models import CloudinaryField


class DollType(models.Model):
    """ A model to manage doll categories """

    name = models.CharField(max_length=25, null=False, blank=False)

    def __str__(self):
        return self.name


class Doll(models.Model):
    """ A model to manage all dolls """

    name = models.CharField(max_length=100, null=False, blank=False)
    category = models.ForeignKey(DollType, on_delete=models.CASCADE, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = CloudinaryField('image', default='placeholder')
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    certification = models.CharField(max_length=100, null=False, blank=False)
    safety_note = models.TextField(null=False, blank=False)
    size = models.CharField(max_length=100, null=False, blank=False)
    materials = models.CharField(max_length=150, null=False, blank=False)
    care_love_instructions = models.TextField(null=False, blank=False)
    on_sale = models.BooleanField(default=False, blank=False)

    def __str__(self):
        return self.name
