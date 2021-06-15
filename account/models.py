from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,first_name,last_name,password=None):
        if not email:
            raise ValueError('user must have an email')

        if not username:
            raise ValueError('user must have an username')

        user=self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,first_name,last_name,password):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email=models.EmailField(max_length=250,unique=True)
    username=models.CharField(max_length=250,unique=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)

    #required
    is_active=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)
    login_date=models.DateTimeField(auto_now_add=True)
    joined_date=models.DateTimeField(auto_now=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name']

    objects=MyAccountManager()

    def has_perm(self,obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True