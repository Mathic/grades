from django.conf.urls import url

from . import views
from .views import AssignmentDetail, SectionDetail, CourseDetail, \
    AssignmentCreate, SectionCreate, CourseCreate, \
    AssignmentUpdate, SectionUpdate, CourseUpdate, \
    AssignmentDelete, SectionDelete, CourseDelete

app_name = 'calculate'
urlpatterns = [

    url(r'^$', views.index, name='index'),

    # ex: /calculate/course_details/5
    url(r'^course_detail/(?P<pk>\d+)/$', CourseDetail.as_view(), name='course_detail'),
    # ex: /calculate/add_course
    url(r'^add_course/$', CourseCreate.as_view(), name='add_course'),
    url(r'^delete_course/(?P<pk>\d+)/$', CourseDelete.as_view(), name='delete_course'),
    url(r'^update_course/(?P<pk>\d+)/$', CourseUpdate.as_view(), name='update_course'),

    # ex: /calculate/section_details/5
    url(r'^section_detail/(?P<pk>\d+)/$', SectionDetail.as_view(), name='section_detail'),
    # ex: /calculate/add_section/Course/4/
    url(r'^add_section/(?P<s_type>.+)/(?P<pk>[0-9]+)/$', SectionCreate.as_view(), name='add_section'),
    url(r'^delete_section/(?P<pk>\d+)/$', SectionDelete.as_view(), name='delete_section'),
    url(r'^update_section/(?P<pk>\d+)/$', SectionUpdate.as_view(), name='update_section'),

    # ex: /calculate/assignment_details/5
    url(r'^assignment_detail/(?P<pk>\d+)/$', AssignmentDetail.as_view(), name='assignment_detail'),
    # ex: /calculate/add_assignment
    url(r'^add_assignment/$', AssignmentCreate.as_view(), name='add_assignment'),
    # ex: /calculate/add_section/Section/4/
    url(r'^add_assignment/(?P<pk>\d+)/$', AssignmentCreate.as_view(), name='add_assignment'),
    url(r'^delete_assignment/(?P<pk>\d+)/$', AssignmentDelete.as_view(), name='delete_assignment'),
    url(r'^update_assignment/(?P<pk>\d+)/$', AssignmentUpdate.as_view(), name='update_assignment'),
]
