from django.db import models

from projectaccount.models import Account


# Create your models here.



class Student(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    register_number = models.IntegerField(null=True,blank=True)
    roll_number = models.IntegerField(null=True,blank=True)


class SeriesExam(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)

class Questions(models.Model):
    teacher = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="teacher", null=True, blank=True)
    exam_name = models.ForeignKey(SeriesExam, on_delete=models.CASCADE, related_name="series_exam", null=True, blank=True)
    question_one = models.IntegerField(null=True,blank=True)
    question_one_co = models.CharField(max_length=5,null=True,blank=True)
    question_two = models.IntegerField(null=True,blank=True)
    question_two_co = models.CharField(max_length=5,null=True,blank=True)
    question_three = models.IntegerField(null=True,blank=True)
    question_three_co = models.CharField(max_length=5,null=True,blank=True)
    question_four = models.IntegerField(null=True,blank=True)
    question_four_co = models.CharField(max_length=5,null=True,blank=True)
    question_five = models.IntegerField(null=True,blank=True)
    question_five_co = models.CharField(max_length=5,null=True,blank=True)
    question_six = models.IntegerField(null=True,blank=True)
    question_six_co = models.CharField(max_length=5,null=True,blank=True)
    question_seven = models.IntegerField(null=True,blank=True)
    question_seven_co = models.CharField(max_length=5,null=True,blank=True)
    question_eight = models.IntegerField(null=True,blank=True)
    question_eight_co = models.CharField(max_length=5,null=True,blank=True)
    question_nine = models.IntegerField(null=True,blank=True)
    question_nine_co = models.CharField(max_length=5,null=True,blank=True)
    question_ten = models.IntegerField(null=True,blank=True)
    question_ten_co = models.CharField(max_length=5,null=True,blank=True)
