from django import forms
from django.forms import ModelForm
from .models import Classroom

class ClassroomForm(ModelForm):
    class Meta:
        model = Classroom
        fields = ['course_name', 'course_block','class_list']
    
##    def clean_course_block(self):
##        course_block = self.cleaned_data['course_block']
##        if Classroom.objects.filter(course_block=course_block).filter(teacher=request.user).exclude(pk=self.instance.pk).exists():
##            raise ValidationError('This course block is already used.')
##        return course_block


class DeleteForm(ModelForm):
    class Meta:
        model = Classroom
        fields = ['course_block']
