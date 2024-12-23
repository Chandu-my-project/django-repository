from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

# Create your models here.
class Institutes(models.Model):
    iname=models.CharField(max_length=100)
    #whenever new column is added use default
    founder=models.CharField(max_length=100,default='')
    picture=models.FileField()
    type=models.CharField(max_length=100)
    location=models.CharField(max_length=100,default='')
    #rating=
    def __str__(self):
        return self.iname

class Course(models.Model):
    institute=models.ForeignKey(Institutes,default=1,on_delete=models.SET_DEFAULT)
    cname=models.CharField(max_length=100)
    fees=models.FloatField(max_length=10000000)
    no_of_seats=models.IntegerField()
    is_favorite=models.BooleanField(default=False)
    overall_rating=models.IntegerField(null=True,blank=True)
    #graph=models.ImageField(default='',upload_to='media',blank=True)
    #sentiment=models.CharField(max_length=1000,default='',blank=True,null=True)
    pos=models.IntegerField(null=True,blank=True,default=0)
    neg=models.IntegerField(null=True,blank=True,default=0)
    neu=models.IntegerField(null=True,blank=True,default=0)
    def __str__(self):
        return self.cname

class Feedback(models.Model):
    deg_inst = models.ForeignKey(Institutes, on_delete=models.CASCADE, null=True, blank=True)
    course=models.ForeignKey(Course,default=1,on_delete=models.SET_DEFAULT)
    deg_level= models.CharField(max_length=20, default='')
    enroll_status=models.CharField(max_length=20, default='')
    grad_year=models.PositiveIntegerField(default=current_year(),validators=[MinValueValidator(1985), max_value_current_year], null=True)
    class_env=models.CharField(max_length=20, default='')
    review=models.TextField()
    pname=models.CharField(max_length=100)
    sentiment = models.CharField(max_length=1000,default='')
    star1=models.IntegerField(null=True)
    star2 = models.IntegerField(null=True)
    star3 = models.IntegerField(null=True)
    rating = models.IntegerField(null=True)
    tot_rating=models.IntegerField(null=True)
    def __str__(self):
        return self.pname+"-"+self.review

class rev(models.Model):
    review=models.TextField()
    # pname=models.CharField(max_length=100)
    sentiment = models.CharField(max_length=1000,default='')
    rating = models.IntegerField(null=True)

    def __str__(self):
        return self.review