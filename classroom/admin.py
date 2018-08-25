from django.contrib import admin

from .models import Classroom, Student


class StudentAdmin(admin.ModelAdmin):
    fields = ('nickname',)
    list_display = ('nickname',)
    list_filter = ('classroom',)

admin.site.register(Student, StudentAdmin)
