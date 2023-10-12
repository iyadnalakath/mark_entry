from django.contrib import admin

from projectaccount.models import Subject
from store.models import Student



# Register your models here.


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(Subject, SubjectAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(Student, StudentAdmin)
