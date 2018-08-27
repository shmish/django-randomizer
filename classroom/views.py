from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from django.shortcuts import get_object_or_404, Http404, render, get_list_or_404
#from django.forms import ModelForm
from django.views.generic.edit import CreateView, FormView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.shortcuts import render

import json
from .models import Classroom, Student, StudentFilter
from .forms import ClassroomForm, DeleteForm

def index(request):
    nickname_list = Classroom.objects.order_by('nickname')
    context = {'nickname_list': nickname_list}
    return render(request, 'classroom/index.html', context)

@login_required
def submitted(request):
    return render(request, 'classroom/submitted.html')

class ClassroomCreateView(LoginRequiredMixin, CreateView):
    #login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Classroom
    form_class = ClassroomForm
    
    def form_valid(self, form):
        f = form.save(commit=False)
        f.teacher = self.request.user
        f.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('classroom:blocklist')

create_classroom_view = ClassroomCreateView.as_view()


class BlockListView(LoginRequiredMixin, ListView):
    #login_url = 'accounts/login/'
    redirect_field_name = 'redirect_to'
    model= Classroom

    def get_context_data(self, **kwargs):
        context = super(BlockListView, self).get_context_data(**kwargs)
        classroom_blocks = Classroom.objects.filter(teacher=self.request.user)
        context = {'classroom_blocks': classroom_blocks}
        return context

list_classroom_view = BlockListView.as_view()

class BlockDeleteView(LoginRequiredMixin, DeleteView):
    #login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Classroom
    success_url = reverse_lazy('classroom:blocklist')

delete_classroom_view = BlockDeleteView.as_view()

class BlockUpdateView(LoginRequiredMixin, UpdateView):
    #login_url = '/login/'
    #redirect_field_name = 'redirect_to'    
    model = Classroom
    fields = ['class_list']
    #fields = ['course_name', 'course_block', 'class_list']
    success_url = reverse_lazy('classroom:blocklist')
    
update_classroom_view = BlockUpdateView.as_view()

@login_required
def random(request):
    classroom = Classroom.objects.filter(teacher=request.user).order_by('course_block')
    classblock = request.GET.get('class_block')
    cblock = Classroom.objects.all().filter(course_block=classblock)
    cblocknum = cblock.count()
    students = Student.objects.all().filter(classroom__course_block=classblock)
    nicknames = [s.nickname for s in students]
    data = serializers.serialize("json", students, fields = ("nickname", "attend"))
    student_names = json.dumps(list(nicknames))
    context = {'students': students}
    context['classroom'] = classroom
    context['cblock'] = cblock
    context['student_names'] = student_names
    context['cblocknum'] = cblocknum
    context['data'] = data
    template = loader.get_template('classroom/randomize.html')
    print (data)
    return render(request, 'classroom/randomize.html', context)

@login_required
def block_delete(request, id):
    obj = get_list_or_404()
    context = {"object": obj}
    return render(request, "classroom_confirm_delete.html", context)

@login_required
def student_list(request):
    s = StudentFilter(request.GET, queryset=Student.objects.all())
    # f = AttendFilter(request.GET, queryset=Student.objects.all())
    return render(request, 'classroom/student_list.html', {'filter': s})
    # return render(request, 'classroom/student_list.html', {'filter2': f})

class ClassroomDetailView(LoginRequiredMixin, DetailView):
    #login_url = '/login/'
    redirect_field_name = 'redirect_to'    
    model = Classroom
    template_name = 'classroom/random_list.html'

    def get_context_data(self, **kwargs):
        class_pk = self.kwargs['pk']
        context = super(ClassroomDetailView, self).get_context_data(**kwargs)
        students = Student.objects.filter(pk = 'class_pk')
        context['students'] = students
        return context

detail_classroom_view = ClassroomDetailView.as_view()

##def register_success(request):
##    return render_to_response('registration/success.html',)
## 
##def logout_page(request):
##    logout(request)
##    return HttpResponseRedirect('/')
