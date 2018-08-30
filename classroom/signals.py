from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from .models import Classroom, Student

@receiver(post_save, sender=User)
def post_save_user_signal_handler(sender, instance, created, **kwargs):
    if created:
       instance.is_staff = True
       teach = Group.objects.get(name='Teachers')
       instance.groups.add(teach)
       instance.save()
       
##@receiver(post_save, sender=Classroom)
##def post_save_classroom_makestudents(sender,instance, **kwargs):
##        print(Classroom.class_list)
##        studentList = []
##        studentList = Classroom.class_list.split('\n')
##        for line in studentList:
##            line = line.strip('\r')
##            s = Student.objects.create(nickname = line, attend = True, classroom = self)
