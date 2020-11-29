from django.db import models
#user model extensions
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


#custom auth user model
#provides help function for creating a user or creating a superuser
class UserManager(BaseUserManager):
    #overriding certain logic in create_user method   
    #custom handle the email address. Anything extra becomes add'l fields in user
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address.')
        #creates a new user model
        user = self.model(email=self.normalize_email(email), **extra_fields)
        #pw is encrypted so need to use set_password method
        user.set_password(password)
        #self.db used for supporting mulitple databases, but still good practice with only one
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        """Creates and save new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    #assign user manager to objs attribute
    objects = UserManager()
    #customize and replace username field to email
    USERNAME_FIELD = 'email'


