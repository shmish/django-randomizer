from django.conf.urls import url, include
from django.urls import path
from . import views
from classroom.views import create_classroom_view, list_classroom_view, delete_classroom_view, update_classroom_view

app_name = "classroom"
urlpatterns = [
    path('', views.index, name='index'),
    path('submitted', views.submitted, name='submitted'),
    #path('classup/', create_classroom_view, name='classroom'),
    path('classup/', views.get_classlist, name='classroom'),
    path('random/', views.random, name='random'),
    #path('block/', views.block, name='block'),
    path('blocklist/', list_classroom_view, name='blocklist'),
    path('<int:pk>/blockDelete/', delete_classroom_view, name='blockDelete'),
    path('<int:pk>/blockUpdate/', update_classroom_view, name='blockUpdate'),
    #path('random/', views.block, name='random'),
    #url(r'^accounts/', include('allauth.urls')),
    #path('accounts/', allauth.urls),
]

    #path(r'^deleteblock/$', delete_block_view, name='deleteblock'),
    #path(r'^adjust/$', views.adjust, name='adjust')