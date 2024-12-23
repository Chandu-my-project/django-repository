from django.db import models

# Create your models here.
class student_points(models.Model):
    personality_number=models.CharField(max_length=50)
    points=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.personality_number

class personality(models.Model):
    personality_type=models.CharField(max_length=100,null=True,blank=True)
    personality_des=models.TextField(max_length=10000,null=True,blank=True)
    # per=models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.personality_type

class cluster(models.Model):
    cluster_name=models.CharField(max_length=100)
    cluster_des=models.TextField(max_length=10000)
    clipart = models.ImageField(default='', upload_to='media', blank=True)
    def __str__(self):
        return self.cluster_name

class personality_cluster(models.Model):
    personality=models.CharField(max_length=100)

    career_cluster=models.ForeignKey(cluster,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.career_cluster.cluster_name

class cluster_major(models.Model):
    career_cluster = models.ForeignKey(cluster, on_delete=models.CASCADE, null=True, blank=True)
    major=models.CharField(max_length=100)

    def __str__(self):
        return self.major
