from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator




def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    edu_level = models.CharField(max_length=100, default="")
    #status = models.CharField(max_length=100, default="")
    grad_year = models.PositiveIntegerField(default=current_year(),validators=[MinValueValidator(1985), max_value_current_year], null=True)
    dob = models.DateField(max_length=8, null=True)
    college_name = models.CharField(max_length=100, default='')
    # major=models.CharField(max_length=100,default="")
    # combo=models.CharField(max_length=100,default="")

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    college_name=models.CharField(max_length=100,default='')
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    edu_level = models.CharField(max_length=100, default="")
    # status = models.CharField(max_length=100, default="")
    grad_year = models.PositiveIntegerField(default=current_year(),validators=[MinValueValidator(1985), max_value_current_year], null=True)
    dob = models.DateField(max_length=8, null=True)
    # major=models.CharField(max_length=100,default="")
    # combo = models.CharField(max_length=100, default="")


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    college_name = models.CharField(max_length=100)
    # designation = models.CharField(max_length=100)
