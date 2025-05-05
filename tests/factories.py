from factory import LazyAttribute, faker, post_generation
from factory.django import DjangoModelFactory

from app.models import Constructor, Driver, Nationality


class DriverFactory(DjangoModelFactory):
    ref = LazyAttribute(lambda r: f"{r.surname.lower()}")
    number = faker.Faker("pyint", max_value=99)
    code = LazyAttribute(lambda c: f"{c.surname[:3].upper()}")
    forename = faker.Faker("first_name")
    surname = faker.Faker("last_name")
    date_of_birth = faker.Faker("date_time_this_century")
    nationality = faker.Faker("random_element", elements=Nationality.objects.all())
    url = faker.Faker("url")

    class Meta:
        model = Driver

    @post_generation
    def set_name_in_url(self, create, extracted, **kwargs):
        if not create and not extracted:
            return
        self.url = f"{self.url}/{self.surname.lower()}_{self.forename.lower()}/"


class ConstructorFactory(DjangoModelFactory):
    ref = LazyAttribute(lambda r: f"{r.name.lower()}")
    name = faker.Faker("last_name_nonbinary")
    nationality = faker.Faker("random_element", elements=Nationality.objects.all())

    class Meta:
        model = Constructor

    @post_generation
    def set_constructor_manufacture_name_in_url(self, create, extracted, **kwargs):
        if not create and not extracted:
            return
        self.url = f"https://{self.name.lower()}.com/"

