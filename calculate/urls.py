from . import views

from django.conf.urls import url
from .views import SectionDelete, CourseDelete, AssignmentDelete

app_name = 'calculate'
urlpatterns = [

    url(r'^$', views.index, name='index'),

    # ex: /calculate/course_details/5
    url(r'^course_details/(?P<course_id>[0-9]+)/$', views.course_details, name='course_details'),
    # ex /calculate/add_course
    url(r'^add_course/$', views.add_course, name='add_course'),
    url(r'^delete_course/(?P<pk>\d+)/$', CourseDelete.as_view(), name='delete_course'),

    # ex: /calculate/section_details/5
    url(r'^section_details/(?P<section_id>[0-9]+)/$', views.section_details, name='section_details'),
    # ex /calculate/add_section
    url(r'^add_section/$', views.add_section, name='add_section'),
    # ex /calculate/add_section/Course/4/
    url(r'^add_section/(?P<s_type>.+)/(?P<pk>[0-9]+)/$', views.add_section, name='add_section'),
    url(r'^delete_section/(?P<pk>\d+)/$', SectionDelete.as_view(), name='delete_section'),

    # ex: /calculate/assignment_details/5
    url(r'^assignment_details/(?P<assignment_id>[0-9]+)/$', views.assignment_details, name='assignment_details'),
    # ex /calculate/add_assignment
    url(r'^add_assignment/$', views.add_assignment, name='add_assignment'),
    # ex /calculate/add_section/Section/4/
    url(r'^add_assignment/(?P<pk>[0-9]+)/$', views.add_assignment, name='add_assignment'),
    url(r'^delete_assignment/(?P<pk>\d+)/$', AssignmentDelete.as_view(), name='delete_assignment'),
]
