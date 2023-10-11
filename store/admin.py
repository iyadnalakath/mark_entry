from django.contrib import admin

from store.models import Subject

# Register your models here.


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(Subject, SubjectAdmin)
