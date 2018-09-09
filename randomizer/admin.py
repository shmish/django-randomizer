from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Classroom, Student

class ClassListFilter(admin.SimpleListFilter):
    title = _('in classroom')
    
    # I"m not sure what this parameter refers to
    parameter_name = 'classroom'
    
    def lookups(self, request, model_admin):
        return (
            ('1-1', _('Block 1-1')),
            ('1-2', _('Block 1-2')),
            ('1-3', _('Block 1-3')),
            ('1-4', _('Block 1-4')),
            ('2-1', _('Block 2-1')),
            ('2-2', _('Block 2-2')),
            ('2-3', _('Block 2-3')),
            ('2-4', _('Block 2-4')),
    
        )
    
    def queryset(self, request, queryset):
        if request.user.is_superuser:
            return queryset.all()
        else:
            blocks = {'11':'1-1','12':'1-2','13':'1-3','14':'1-4','21':'2-1','22':'2-2','23':'2-3','24':'2-4'}
            for k, v in blocks.items():
                if self.value() == v:
                    return queryset.filter(classroom__teacher=request.user,
                                           classroom__course_block=str(k))
def get_loggedUser(self,request):
    logged_in = request.user
    if logged_in.is_superuser:
        return True
    else:
        return False
    
class StudentAdmin(admin.ModelAdmin):
    fields = ('nickname', 'student_first',)
    list_display = ('nickname',)
    #list_filter = ('classroom__teacher',)
    list_filter = (ClassListFilter,)
    if get_loggedUser:
        list_filter = ('classroom__teacher',)
    else:
        list_filter = (ClassListFilter,)
         
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
