from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_save

class UserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, nickname, password=None):

        if not email or not nickname or not password:
            raise ValueError("required email, nickname, password")
        
        user = self.model(
                email = self.normalize_email(email),
                nickname = nickname
                )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nickname,  password=None):

        if not email or not nickname or not password:
            raise ValueError("required email, nickname, password")
        user = self.create_user(
            email = self.normalize_email(email),
            nickname = nickname,
            password=password
        )
        print (dir(user))
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class ttokttokCarUser(AbstractBaseUser, PermissionsMixin):

    objects = UserManager()

    email = models.EmailField(
            max_length=255,
            unique=True,
            )
    nickname = models.CharField(
            max_length=20,
            null=False,
            unique=True
            )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['email']
