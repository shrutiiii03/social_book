from django.test import TestCase
from accounts.models import CustomUser

class CustomUserModelTest(TestCase):
    def test_custom_user_fields(self):
        user = CustomUser.objects.create_user(
            username="testuser",
            email="test@example.com",
            birth_year=1990,
            address="123 Street"
        )
        self.assertEqual(user.age, 2025 - 1990)  
        self.assertEqual(user.public_visibility, True) 
        self.assertEqual(user.address, "123 Street")

