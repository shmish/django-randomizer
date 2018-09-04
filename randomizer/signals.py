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
       
