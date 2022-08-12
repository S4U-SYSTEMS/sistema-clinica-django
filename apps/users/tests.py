from django.test import TestCase

from .models import User

class UserTestBase(TestCase):
    def setUp(self) -> None:
        user = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='username@email.com',
        )
        return super().setUp()


