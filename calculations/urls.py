from django.conf.urls import url

from . import views
from .views import CourseCreate, CourseUpdate, CourseDelete, CourseView, \
    AssignmentCreate, AssignmentUpdate, AssignmentDelete, IndexView

app_name = 'calculations'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),

    # ex: /calculate/course_details/5
    url(r'^view_course/(?P<pk>\d+)/$', CourseView.as_view(), name='view_course'),
    # ex: /calculate/add_course
    url(r'^add_course/$', CourseCreate.as_view(), name='add_course'),
    url(r'^delete_course/(?P<pk>\d+)/$', CourseDelete.as_view(), name='delete_course'),
    url(r'^update_course/(?P<pk>\d+)/$', CourseUpdate.as_view(), name='update_course'),

    # ex: /calculate/add_assignment/0/4/
    url(r'^add_assignment/(?P<is_section>\d+)/(?P<pk>\d+)/$', AssignmentCreate.as_view(), name='add_assignment'),
    url(r'^ajax/update_assignment_list/', views.update_assignment_list, name='update_assignment_list'),
    url(r'^delete_assignment/(?P<pk>\d+)/$', AssignmentDelete.as_view(), name='delete_assignment'),
    url(r'^update_assignment/(?P<pk>\d+)/$', AssignmentUpdate.as_view(), name='update_assignment'),
]
