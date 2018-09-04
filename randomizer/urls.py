from django.conf.urls import url, include
from django.urls import path
from . import views
from randomizer.views import create_classroom_view, list_classroom_view, delete_classroom_view, update_classroom_view

app_name = "randomizer"
urlpatterns = [
    path('', views.index, name='index'),
    path('submitted', views.submitted, name='submitted'),
    path('classup/', views.get_classlist, name='classroom'),
    path('random/', views.random, name='random'),
    path('blocklist/', list_classroom_view, name='blocklist'),
    path('<int:pk>/blockDelete/', delete_classroom_view, name='blockDelete'),
    path('<int:pk>/blockUpdate/', update_classroom_view, name='blockUpdate'),

]

