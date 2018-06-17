from django.conf.urls import url

from . import views


app_name = 'school'
urlpatterns = [
    url(r'^$', views.display_teachers, name='teachers'),
    url(r'teacher/(?P<teacher_id>[0-9]+)', views.get_teacher_info, name='teacher'),
    url(r'add/', views.add, name='add'),
    url(r'delete/(?P<teacher_id>[0-9]+)', views.delete, name='delete'),
    url(r'update/(?P<teacher_id>[0-9]+)', views.update, name='update'),
]
