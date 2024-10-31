from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from companies.models import Company


class CustomBaseUserManager(BaseUserManager):
    
    def _create_user(self, email ,password,  **extra_fields):
        if not email :
            raise ValueError("email must be provided")
        if not password:
            raise ValueError('Password is not provided')
        email = self.normalize_email(email)
        user = self.model(
            email=email ,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email,  **extra_fields):
        extra_fields.setdefault('is_staff',False)
    
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email, **extra_fields)

    def create_superuser(self, email ,  **extra_fields):
        extra_fields.setdefault('is_staff',True)
   
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email,  **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(max_length=40,null=True,blank=True)
    company = models.ForeignKey(Company, related_name='users', on_delete=models.SET_NULL, null=True, blank=True)
    last_name = models.CharField(max_length=40,null=True,blank=True)
    cellphone_number = models.TextField(max_length=13,blank=True,null=True)
    email = models.EmailField(unique=True,null=True,blank=True)
   
    # password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True,null=True)
    date_joined = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    is_coach = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_registration_complete = models.BooleanField(default=False)



    objects = CustomBaseUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']










