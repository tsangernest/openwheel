from django.db import models


class Nationality(models.Model):
    demonym = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["demonym"]

    def __str__(self) -> str:
        return f"{self.demonym}"

