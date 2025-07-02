from functools import cached_property

from django.db import models

from app.managers import _DeprecatedManager, NationalityManager


class Nationality(models.Model):
    demonym = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = NationalityManager()
    deprecated_objects = _DeprecatedManager()

    class Meta:
        ordering = ["demonym"]

    def __str__(self):
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
        return f"[{self.surname}, {self.forename}]"


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


class Race(models.Model):
    name = models.CharField(max_length=255)
    circuit = models.ForeignKey(to="Circuit", on_delete=models.DO_NOTHING)
    date_of_race = models.DateTimeField()
    round_number = models.PositiveIntegerField()
    url = models.URLField(blank=True)

    class Meta:
        ordering = ["-date_of_race"]

    def __str__(self):
        return f"{self.date_of_race.year} - {self.name}"


class Qualifying(models.Model):
    race = models.ForeignKey(to="Race", on_delete=models.DO_NOTHING, related_name="quali")
    driver = models.ForeignKey(to="Driver", on_delete=models.DO_NOTHING)
    constructor = models.ForeignKey(to="Constructor", on_delete=models.DO_NOTHING)
    position = models.PositiveIntegerField()
    q_one = models.DurationField(blank=True, null=True)
    q_two = models.DurationField(blank=True, null=True)
    q_three = models.DurationField(blank=True, null=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.race}, {self.driver}, start_grid_position={self.position}"


class LapTime(models.Model):
    race = models.ForeignKey(to="Race", on_delete=models.DO_NOTHING, related_name="lap_times")
    driver = models.ForeignKey(to="Driver", on_delete=models.DO_NOTHING)
    lap_number = models.PositiveIntegerField()
    position = models.PositiveIntegerField()
    time = models.DurationField(blank=True, null=True)

    class Meta:
        ordering = ["-race"]
    
    def __str__(self):
        return f"{self.race}, {self.driver}, lap_number={self.lap_number}, position={self.position}"


class PitStop(models.Model):
    race = models.ForeignKey(to="Race", on_delete=models.DO_NOTHING, related_name="pit_stops")
    driver = models.ForeignKey(to="Driver", on_delete=models.DO_NOTHING)
    stop_number = models.PositiveIntegerField()
    lap_number = models.PositiveIntegerField()
    local_time = models.TimeField()
    duration = models.DurationField(blank=True, null=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.race}, {self.driver}, stop_number={self.stop_number}, lap_number={self.lap_number}"


class DriverStanding(models.Model):
    race = models.ForeignKey(to="Race", on_delete=models.DO_NOTHING)
    driver = models.ForeignKey(to="Driver", on_delete=models.DO_NOTHING)
    points = models.PositiveIntegerField()
    number_of_wins = models.PositiveIntegerField()

    class Meta:
        ordering = ["id"]


class ConstructorStanding(models.Model):
    race = models.ForeignKey("Race", models.DO_NOTHING)
    constructor = models.ForeignKey("Constructor", models.DO_NOTHING)
    points = models.PositiveIntegerField()
    number_of_wins = models.PositiveIntegerField()

    class Meta:
        ordering = ["id"]


class DropStuff(models.Model):
    file = models.BinaryField(blank=True, editable=True)
    file_name = models.CharField(max_length=255)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.file_name}"

