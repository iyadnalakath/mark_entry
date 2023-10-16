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
    teacher = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="teacher_name", null=True, blank=True)
    exam_name = models.ForeignKey(SeriesExam, on_delete=models.CASCADE, related_name="series", null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student_name", null=True, blank=True)
    question_1 = models.IntegerField(null=True,blank=True)
    question_one_co = models.CharField(max_length=5,null=True,blank=True)
    question_2 = models.IntegerField(null=True,blank=True)
    question_two_co = models.CharField(max_length=5,null=True,blank=True)
    question_3 = models.IntegerField(null=True,blank=True)
    question_three_co = models.CharField(max_length=5,null=True,blank=True)
    question_4 = models.IntegerField(null=True,blank=True)
    question_four_co = models.CharField(max_length=5,null=True,blank=True)
    question_5 = models.IntegerField(null=True,blank=True)
    question_five_co = models.CharField(max_length=5,null=True,blank=True)
    question_6 = models.IntegerField(null=True,blank=True)
    question_six_co = models.CharField(max_length=5,null=True,blank=True)
    question_7 = models.IntegerField(null=True,blank=True)
    question_seven_co = models.CharField(max_length=5,null=True,blank=True)
    question_8 = models.IntegerField(null=True,blank=True)
    question_eight_co = models.CharField(max_length=5,null=True,blank=True)
    question_9 = models.IntegerField(null=True,blank=True)
    question_nine_co = models.CharField(max_length=5,null=True,blank=True)
    question_10 = models.IntegerField(null=True,blank=True)
    question_ten_co = models.CharField(max_length=5,null=True,blank=True)
