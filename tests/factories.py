from factory import SubFactory, faker, lazy_attribute, post_generation
from factory.django import DjangoModelFactory

from app.models import Driver, Nationality


class DriverFactory(DjangoModelFactory):
    nationality = faker.Faker("random_element", elements=Nationality.objects.all())
    number = faker.Faker("pyint", max_value=99)
    forename = faker.Faker("first_name")
    surname = faker.Faker("last_name")
    date_of_birth = faker.Faker("date_time_this_century")

    @lazy_attribute
    def ref(self):
        return f"{self.surname.lower()}"

    @lazy_attribute
    def code(self):
        return f"{self.surname[:3]}"

    class Meta:
        model = Driver

