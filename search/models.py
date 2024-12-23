from django.db import models

# Create your models here.
class DegreeInstitution(models.Model):
    State=models.CharField(max_length=100)
    Degree_Course=models.CharField(max_length=100)
    Institute_name=models.CharField(max_length=200)
    Location = models.CharField(max_length=100)
    Total_Fees = models.CharField(max_length=100)
    Ranked = models.CharField(max_length=100)
    is_favorite=models.BooleanField(default=False,blank=True)
    person_name=models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.Degree_Course+'-'+self.Institute_name