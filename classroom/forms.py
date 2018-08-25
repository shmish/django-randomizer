from django import forms
from django.forms import ModelForm
from .models import Classroom

class ClassroomForm(ModelForm):
    class Meta:
        model = Classroom
        fields = ['course_name', 'course_block','class_list']
    
    def clean_course_block(self):
        course_block = self.cleaned_data['course_block']
        if Classroom.objects.filter(course_block=course_block).exclude(pk=self.instance.pk).exists():
            raise ValidationError('This course block is already used.')
        return course_block

##    def clean(self):
##        #cleaned_data = super().clean()
##        print("Try this")
##        print(self.cleaned_data)
##        print(self.errors)
##        try:
##            Classroom.objects.get(course_block=self.cleaned_data['course_block'])
##            #cleaned_data.get("course_block")
##            print(self.cleaned_data)
##            print(self.errors)
##            self.redirect = True
##            raise forms.ValidationError("Exists already")
##        except Classroom.DoesNotExist:
##            pass
##        return self.cleaned_data

class DeleteForm(ModelForm):
    class Meta:
        model = Classroom
        fields = ['course_block']
