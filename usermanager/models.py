from django.db import models
from django.contrib.auth import models as auth_models
# Create your models here.


# AbstractBaseUser
# BaseUserManager

class UserManager(auth_models.BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):

        "Creates and saves a new user"

        if not email:
            raise ValueError(('Users must have an email address'))

        user = self.model(email=self.normalize_email(email), **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):

        "Creates and saves a new superuser"

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

class User(auth_models.AbstractBaseUser, models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200,unique=True)
    phone = models.CharField(max_length=15)
    dob = models.CharField(max_length=20)

    # Mondatory things 
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=True)


    is_admin = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'


    objects = UserManager()
        
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
  






