from functools import cached_property

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
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField(blank=True)
    nationality = models.ForeignKey(to="Nationality", on_delete=models.DO_NOTHING, blank=True)
    url = models.URLField(blank=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.surname}, {self.forename}"


class Constructor(models.Model):
    ref = models.CharField(blank=True, max_length=255)
    name = models.CharField(max_length=255)
    nationality = models.ForeignKey(to="Nationality", on_delete=models.DO_NOTHING, blank=True)
    url = models.URLField(blank=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.name}"


class Circuit(models.Model):
    ref = models.CharField(blank=True, max_length=255)
    name = models.CharField(max_length=255)
    location = models.CharField(blank=True, max_length=255)
    country = models.ForeignKey(to="Nationality", on_delete=models.DO_NOTHING, blank=True)
    longitude = models.DecimalField(blank=True, max_digits=32, decimal_places=16)
    latitude = models.DecimalField(blank=True, max_digits=32, decimal_places=16)
    altitude = models.IntegerField(blank=True, help_text="Measured in meters")
    url = models.URLField(blank=True)

    class Meta:
        ordering = ["id"]

    @cached_property
    def coordinates(self):
        return f"{self.longitude}, {self.latitude}"

    def __str__(self):
        return f"{self.name}"

