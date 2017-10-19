from .models import Assignment, Course, Section

from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_code', 'course_text', 'type']


class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = ['id', 'section_text', 'percentage', 'type']
        course = forms.ChoiceField(
            choices=[(x.id, x.course_text) for x in Course.objects.all()]
        )
        labels = {
            'percentage': _('Percentage'),
        }
        help_texts = {
            'percentage': _('Your mark percentage for this section in the course.'),
        }

        def save(self, commit=True):
            instance = super().save(commit=False)
            cid = self.cleaned_data['course']
            instance.course = Course.objects.get(pk=cid)
            instance.save(commit)
            return instance


class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ['assignment_name', 'mark', 'total', 'percentage']
