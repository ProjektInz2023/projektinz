from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, Group
from django.utils import timezone


class Alergen(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class MainCourse(models.Model):
    mainCourseId = models.AutoField(primary_key=True, db_column='mainCourseId')
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    alergens = models.ManyToManyField(Alergen, blank=True)
    price = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'main_course'
        
    @staticmethod
    def get_main_course(main_course_id: int):
        try:
            main_course = MainCourse.objects.get(mainCourseId=main_course_id)
            return main_course
        except MainCourse.DoesNotExist:
            return None

    def update_main_course(self, name=None, description=None, price=None):
        if name:
            self.name = name
        if description:
            self.description = description
        if price:
            self.price = price
        self.save()

    def delete_main_course(self):
        self.delete()

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
        verbose_name="email",
        max_length=255,
        unique=True
    )
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    created = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    role = models.ForeignKey(Group, on_delete=models.CASCADE, default=2)

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
    
class Order(models.Model):
    STATUS_CHOICES = (
        ('Aktywne', 'Aktywne'),
        ('Gotowe', 'Gotowe'),
        ('Zakonczone', 'Zakonczone'),
    )

    orderId = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(Staff, on_delete=models.CASCADE)
    mainCourse = models.ForeignKey(MainCourse, on_delete=models.SET("Danie usuniete"))
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES)

    def __str__(self):
        return self.user
    
    def __str__(self):
        return f"Order #{self.pk} - {self.user.email}"
