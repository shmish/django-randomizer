from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.forms import ModelForm
from django import forms
import django_filters

class Classroom(models.Model):
    COURSE_NAME = (
        ('MA8', 'Math 8'),
        ('SC10', 'Science 10'),
        ('PH11', 'Physics 11'),
        ('PH12', 'Physics 12'),
    )
    BLOCK_NUMBER = (
        ('11', 'Block 1-1'),
        ('12', 'Block 1-2'),
        ('13', 'Block 1-3'),
        ('14', 'Block 1-4'),
        ('21', 'Block 2-1'),
        ('22', 'Block 2-2'),
        ('23', 'Block 2-3'),
        ('24', 'Block 2-4'),
    )
    class_list = models.TextField()
    #user = models.ForeignKey(User)
    course_name = models.CharField(max_length=20, choices=COURSE_NAME)
    course_block = models.CharField(max_length=10, choices=BLOCK_NUMBER)
    group_size = models.IntegerField(default=3)
    
##    class Meta:
##        unique_together = ('course_block', 'user')

    def __str__(self):
        return self.get_course_block_display()

    def save(self, *args, **kwargs):
        super(Classroom, self).save(*args, **kwargs)
        # overrides the default save function to parse the class list
        studentList = []
        studentList = self.class_list.split('\n')
        
        for line in studentList:
            line = line.strip('\r')
            s = Student.objects.create(nickname = line, attend = True, classroom = self)
            #print (s)
        #print (studentList)
        #print (Student.attend)

class Student(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    student_first = models.CharField(default='John', max_length=30)
    student_last = models.CharField(default='Smith', max_length=30)
    nickname = models.CharField(default='JohnS', max_length=31)
    attend = models.BooleanField(default=True)
    
##    def __str__(self):
##        return self.nickname

##class ClassroomForm(ModelForm):
##    class Meta:
##        model = Classroom
##        fields = ['course_name', 'course_block','class_list']
##
##    def clean(self):
##        try:
##            Classroom.objects.get(course_block=self.cleaned_data['course_block'])
##            self.redirect = True
##            raise forms.ValidationError("Exists already")
##        except Classroom.DoesNotExist:
##            pass
##        return self.cleaned_data
##
##class DeleteForm(ModelForm):
##    class Meta:
##        model = Classroom
##        fields = ['course_block']

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['classroom__course_block']




# class AttendForm(ModelForm):
#     class Meta:
#         model = Classroom
#         fields = ['course_block']
#
#     def __init__(self, *args, **kwargs):
#         super(AttendForm, self).__init__(*args, **kwargs)

# class RandomForm(ModelForm):
#     class Meta:
#         model = Student
#         fields = ['nickname', 'attend']
