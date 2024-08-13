# Create your models here.
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
import uuid
from django.db.models.signals import pre_save

class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        """
        Create and return a `User` with an email, username and password.
        """
        if not email:
            raise ValueError('Users Must Have an email address')

        user = self.model(
            email=self.normalize_email(
                email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name='email address', max_length=50,unique=True)
    name = models.CharField(max_length=155)
    address = models.CharField(max_length=155)
    phone = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "tbl_user"
        verbose_name = 'User'
        verbose_name_plural ='Users'


def hash_password(sender, instance, *args, **kwargs):

    if 'pbkdf2_sha256' in instance.password:
        pass
    else:
        instance.set_password(instance.password)
        instance.save()


pre_save.connect(hash_password, sender=User)



