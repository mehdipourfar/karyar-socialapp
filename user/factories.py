import factory

from user.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

    username = factory.LazyAttribute(
        lambda obj: f'{obj.first_name}.{obj.last_name}'.replace(' ', '.').lower()
    )
