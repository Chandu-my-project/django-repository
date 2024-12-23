from django.db import models


class Subject(models.Model):
    f_key=models.IntegerField(null=True,blank=True)
    sub_name = models.CharField(max_length=100)
    clipart = models.ImageField(default='', upload_to='media', blank=True)
    def __str__(self):
        return self.sub_name


class Degree(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    deg_name = models.CharField(max_length=100)

    def __str__(self):
        return self.deg_name


class Quiz(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    question = models.CharField(max_length=150)
    op1 = models.CharField(max_length=150)
    op2 = models.CharField(max_length=150)
    op3 = models.CharField(max_length=150)
    op4 = models.CharField(max_length=150)
    answer = models.CharField(max_length=150)
    selected_ans = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.question + "-" + self.answer

class Recommendation(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    tot_score = models.IntegerField()
    marks=models.IntegerField()
    rec=models.BooleanField(default=False,blank=True)
    user_name=models.CharField(max_length=100,blank=True,null=True)



