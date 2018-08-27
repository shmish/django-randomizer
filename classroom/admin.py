from django.contrib import admin

from .models import Classroom, Student


class StudentAdmin(admin.ModelAdmin):
    fields = ('nickname', 'user',)
    list_display = ('nickname', 'user',)
    list_filter = ('classroom',)

class ClassroomAdmin(admin.ModelAdmin):
    fields = ('course_block', 'teacher',)
    list_display = ('course_block', 'teacher',)
    
    def get_queryset(self, request):
        qs = super(ClassroomAdmin, self).get_queryset(request)
        return qs.filter(teacher=request.user)
    
##    def save_model(self, request, obj, form, change):
##        obj.teacher = request.user
##        super().save_model(request, obj, form, change)

admin.site.register(Classroom, ClassroomAdmin)

admin.site.register(Student, StudentAdmin)
