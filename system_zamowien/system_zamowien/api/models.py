from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils import timezone



class MyUserManager(BaseUserManager):
    
    def create_user(self, email, name, surname, password=None):

        if not email:
            raise ValueError("Users must have an email address")
        
        user = self.model(
            email = self.normalize_email(email),
            name = name,
            surname = surname
        )

        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, name, surname, password=None):

        user = self.create_user(
            email,
            name,
            surname,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class Staff(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True
    )
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    created = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","surname"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        
        return True
    
    def has_module_perms(self, app_label):
        
        return True

    @property
    def is_staff(self):

        return self.is_admin
