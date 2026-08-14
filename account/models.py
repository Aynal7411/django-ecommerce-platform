from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, mobile, password=None, **extra_fields):
        if not mobile:
            raise ValueError("Mobile number is required")
        mobile = mobile.strip()
        user = self.model(mobile=mobile, **extra_fields)
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile, password=None, **extra_fields):
       extra_fields.setdefault("is_staff", True)
       extra_fields.setdefault("is_superuser", True)
       extra_fields.setdefault("is_active", True)

       if extra_fields.get("is_staff") is not True:
         raise ValueError("Superuser must have is_staff=True.")

       if extra_fields.get("is_superuser") is not True:
           raise ValueError("Superuser must have is_superuser=True.")
       
       if not password:
            raise ValueError("Superuser must have a password.")

       return self.create_user(mobile=mobile, password=password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    mobile_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Mobile number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    mobile = models.CharField(max_length=15, unique=True,db_index=True, validators=[mobile_validator])
    email = models.EmailField(blank=True, null=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ['name']
    
    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.mobile
