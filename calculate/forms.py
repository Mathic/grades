from django.forms import ModelForm

from .models import Assignment, Course, Section


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_code', 'course_text']


class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = ['section_text', 'percentage']


class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ['assignment_name', 'mark', 'total', 'percentage']
