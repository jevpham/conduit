from django.test import TestCase
from .models import User
from .serializers import UserSerializer

# Create your tests here.
class UserModelTest(TestCase):
    # Set up a test user instance
    def setUp(self):
        self.user = User.objects.create(
            name="Test User",
            email="testuser@example.com",
            password="password123"
        )

    # Test the creation of a user
    def test_user_creation(self):
        self.assertEqual(self.user.name, "Test User")
        self.assertEqual(self.user.email, "testuser@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertIsNotNone(self.user.created_at)
        self.assertIsNotNone(self.user.updated_at)

    # Test the string representation of a user
    def test_user_str(self):
        self.assertEqual(str(self.user), "Test User")

class UserSerializerTest(TestCase):
    # Set up test data for the serializer
    def setUp(self):
        self.user_attributes = {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'password': 'password123'
        }
        self.serializer_data = {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'password': 'password123'
        }
        self.user = User.objects.create(**self.user_attributes)
        self.serializer = UserSerializer(instance=self.user)

    # Test that the serializer contains the expected fields
    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(data.keys(), ['id', 'name', 'email', 'password', 'created_at', 'updated_at'])

    # Test the content of the name field in the serializer
    def test_name_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['name'], self.user_attributes['name'])

    # Test the content of the email field in the serializer
    def test_email_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['email'], self.user_attributes['email'])

    # Test the content of the password field in the serializer
    def test_password_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['password'], self.user_attributes['password'])

    # Test the creation of a user using the serializer
    def test_create_user(self):
        serializer = UserSerializer(data=self.serializer_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.name, self.serializer_data['name'])
        self.assertEqual(user.email, self.serializer_data['email'])
        self.assertEqual(user.password, self.serializer_data['password'])
