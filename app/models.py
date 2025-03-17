from django.db import models


class Nationality(models.Model):
    demonym = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["demonym"]

    def __str__(self) -> str:
        return f"{self.demonym}"


class Driver(models.Model):
    ref = models.CharField(blank=True, max_length=255)
    number = models.CharField(blank=True, max_length=255)
    code = models.CharField(blank=True, max_length=6)
    forename = models.CharField(blank=True, max_length=255)
    surname = models.CharField(blank=True, max_length=255)
    date_of_birth = models.DateField(blank=True)
    nationality = models.ForeignKey(to="Nationality", on_delete=models.DO_NOTHING, blank=True)
    url = models.URLField()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.surname}, {self.forename}"

