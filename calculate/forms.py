from django.forms import ModelForm

from .models import Assignment, Course, Section


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_code']


class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = ['section_name', 'percentage']


class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ['assignment_name', 'mark', 'total', 'percentage']
