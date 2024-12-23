from django.db import models
from embed_video.fields import EmbedVideoField


class Discipline(models.Model):
    dname=models.CharField(max_length=100)
    clipart=models.ImageField(default='',upload_to='media',blank=True)
    description=models.TextField(default="",blank=True)
    career_des=models.CharField(max_length=5000,default="",blank=True)
    video = EmbedVideoField(blank=True)

    def __str__(self):
        return self.dname

class Program(models.Model):
    discipline=models.ForeignKey(Discipline,on_delete=models.CASCADE,null=True, blank=True)
    program=models.CharField(max_length=100)

    def __str__(self):
        return self.program

class Career(models.Model):
    discipline=models.ForeignKey(Discipline,on_delete=models.CASCADE,null=True, blank=True)
    job=models.CharField(max_length=100)

    def __str__(self):
        return self.job

class Specialization(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, null=True, blank=True)
    special = models.CharField(max_length=100)

    def __str__(self):
        return self.special
