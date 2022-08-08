from rest_framework import generics, viewsets
from test_app.models import Blog, Car
from random import randint
from django_seed import Seed

car_names = ("Mercedes", "Porche", "Audi", "Honda", "Mitsbushi")

seeder = Seed.seeder()

seeder.add_entity(Car, 100, {
    'name': lambda x: car_names[randint(0, len(car_names) - 1)]
})


def execute():
    seeder.execute()
    print("seeding completed")


