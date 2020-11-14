from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
import django_filters

class Classroom(models.Model):
    GRADE= (
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    )
    COURSE_NAME = (
        ('MA', 'Math'),
        ('SC', 'Science'),
        ('SS', 'Social Studies'),
        ('EN', 'English Language Arts'),
        ('AP', 'Applied Skills'),
        ('PE', 'Phys Ed'),
        ('ML', 'Modern Languages'),
        ('CE', 'Career Ed'),
        ('AR', 'Arts'),
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
    grade = models.CharField(max_length=2, default='8', choices=GRADE)
    
    class Meta:
        unique_together = ('course_block', 'teacher')

    def __str__(self):
        return self.get_course_block_display()
    
    def save(self, *args, **kwargs):
        super(Classroom, self).save(*args, **kwargs)
        # overrides the default save function to parse the class list
        student_list = []
        student_list = self.class_list.split('\n')
        for line in student_list:
            line = line.strip('\r')
            all_names = line.split()
            num_names = len(all_names)
            if num_names == 2:
                last = all_names[1]
            else:
                last = ' '
            nick = all_names[0] + last[:1]
            Student.objects.create(nickname=nick, student_first=all_names[0],
                                   student_last=last, attend=True, classroom=self)

class Student(models.Model):
    #user = models.ForeignKey(teacher, on_delete=models.CASCADE, default=1)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    student_first = models.CharField(default='John', max_length=30)
    student_last = models.CharField(default='Smith', max_length=30)
    nickname = models.CharField(default='JohnS', max_length=31)
    attend = models.BooleanField(default=True)
    do_not_pick = models.BooleanField(default=False)
    

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['classroom__course_block']

