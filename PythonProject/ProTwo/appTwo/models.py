from django.db import models

# Create your models here.
class Branch(models.Model):
    branch = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.branch

class AdmissionStats(models.Model):
    branch_name = models.ForeignKey(Branch, on_delete=models.CASCADE)
    totalIntake = models.IntegerField()
    cutoff = models.IntegerField()
    placementStats = models.IntegerField()

    def __str__(self):
        return str(self.branch_name)

class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default = 0)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text


