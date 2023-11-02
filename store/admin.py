from django.contrib import admin

from projectaccount.models import Subject
from store.models import Questions, SeriesExam, Student



# Register your models here.


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(Subject, SubjectAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(Student, StudentAdmin)


class SeriesExamAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(SeriesExam, SeriesExamAdmin)





class QuestionMarkAdmin(admin.ModelAdmin):
    list_display = (
        
        "id",
        "teacher",
        "exam_name",
        "student",
        "question_1",
        "question_one_co",
        "question_2",
        "question_two_co",
        "question_3",
        "question_three_co",
        "question_4",
        "question_four_co",
        "question_5",
        "question_five_co",
        "question_6",
        "question_six_co",
        "question_7",
        "question_seven_co",
        "question_8",
        "question_eight_co",
        "question_9",
        "question_nine_co",
        "question_10",
        "question_ten_co"
                    
                    )


admin.site.register(Questions, QuestionMarkAdmin)
