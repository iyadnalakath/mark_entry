from django.contrib import admin

from projectaccount.models import Subject
from store.models import Questions, Student



# Register your models here.


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(Subject, SubjectAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(Student, StudentAdmin)




class QuestionMarkAdmin(admin.ModelAdmin):
    list_display = (
        
        "id",
        "teacher",
        "exam_name",
        "student",
        "question_one",
        "question_one_co",
        "question_two",
        "question_two_co",
        "question_three",
        "question_three_co",
        "question_four",
        "question_four_co",
        "question_five",
        "question_five_co",
        "question_six",
        "question_six_co",
        "question_seven",
        "question_seven_co",
        "question_eight",
        "question_eight_co",
        "question_nine",
        "question_nine_co",
        "question_ten",
        "question_ten_co"
                    
                    )


admin.site.register(Questions, QuestionMarkAdmin)
