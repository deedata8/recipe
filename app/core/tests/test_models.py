from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    #tests the customized create_user django helper func
    def test_create_user_with_email_successful(self):
        """Helper function able to create a new user with email"""
        email = 'test@gmail.com'
        password = 'testpass123'
        #this django helper func usually needs a username, the 'create_user' is customized (see models.py)
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email,email)
        #helper django func user.check_password returns boolean
        self.assertTrue(user.check_password(password))

    
    #tests the customized create_user helper func
    def test_new_user_email_normalize(self):
        """Test the email for a new user is normalized @***.com to be case insensitve"""
        email = 'test@GMAIL.com'
        user = get_user_model().objects.create_user(email, 'pwtest123')
        self.assertEqual(user.email, email.lower())

    #tests the customized create_user helper func
    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'pwtest123')

    #tests the NEW func create_superuser
    def test_create_new_superuser(self):
        """Test create new superuser and its attributes"""
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'pwtest123'
        )
        #is_superuser is included in PermissionsMixin
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
