from django.db import models


class Nationality(models.Model):
    demonym = models.CharField(unique=True, max_length=255)
    country = models.CharField(unique=True, max_length=255)

