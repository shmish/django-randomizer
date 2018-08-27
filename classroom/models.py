from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
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
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    course_name = models.CharField(max_length=20, choices=COURSE_NAME)
    course_block = models.CharField(max_length=10, choices=BLOCK_NUMBER)
    group_size = models.IntegerField(default=3)
    
    class Meta:
        unique_together = ('course_block', 'teacher')

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

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    student_first = models.CharField(default='John', max_length=30)
    student_last = models.CharField(default='Smith', max_length=30)
    nickname = models.CharField(default='JohnS', max_length=31)
    attend = models.BooleanField(default=True)
    

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['classroom__course_block']

