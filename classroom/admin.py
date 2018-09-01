from django.contrib import admin

from .models import Classroom, Student


class StudentAdmin(admin.ModelAdmin):
    fields = ('nickname', 'user',)
    list_display = ('nickname',)
    list_filter = ('classroom',)
    
    def get_queryset(self, request):
        qs = super(StudentAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            stfilter = qs.all()
        else:
            stfilter = qs.filter(classroom__teacher=request.user)

        return stfilter

class ClassroomAdmin(admin.ModelAdmin):
    fields = ('course_name', 'grade', 'course_block',)
    list_display = ('course_block', 'course_name', 'grade', 'teacher',)
    
    def get_queryset(self, request):
        qs = super(ClassroomAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            stfilter = qs.all()
        else:
            stfilter = qs.filter(teacher=request.user)
            
        return stfilter
    
admin.site.register(Classroom, ClassroomAdmin)

admin.site.register(Student, StudentAdmin)
