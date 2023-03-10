from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.urls import reverse
# Create your models here.



class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        if not username:
            raise ValueError("Users must have usernames")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password):
        user = self.create_user(
                email = self.normalize_email(email),
                password = password,
                username = username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email",max_length=60,unique=True)
    username = models.CharField(max_length=30,unique=True)
    first_name = models.CharField(max_length=30,unique=False)
    second_name = models.CharField(max_length=30,unique=False)
    date_joined = models.DateTimeField(verbose_name="data joined",auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perms(self,perm,obj=None):
        return self.is_active

    def has_perm(self,perm,obj=None):
        return self.is_active

    def has_module_perms(self,app_label):
        return True

    def get_absolute_url(self):
        return reverse("users:detail_account_view")