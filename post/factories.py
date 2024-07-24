import factory

from user.factories import UserFactory

from post.models import Post


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    user = factory.SubFactory(UserFactory)
    text = factory.Faker("text")
