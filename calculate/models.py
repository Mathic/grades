from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _


# user: spysauce
# password: password123
# Create your models here.
class Course(models.Model):
    course_code = models.CharField(max_length=8, default='PHYS1001')
    course_text = models.CharField(max_length=50)

    def __str__(self):
        return self.course_text


class Section(models.Model):
    section_text = models.CharField(max_length=50)
    percentage = models.IntegerField(default=0,
                                     validators=[
                                         MaxValueValidator(100),
                                         MinValueValidator(1)
                                     ])
    models.ForeignKey('self')
    models.ForeignKey('Course', related_name='course', on_delete=models.CASCADE)

    def __str__(self):
        return self.section_text


class Assignment(models.Model):
    assignment_name = models.CharField(max_length=50)
    mark = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    percentage = models.IntegerField(default=0,
                                     validators=[
                                         MaxValueValidator(100),
                                         MinValueValidator(1)
                                     ])
    models.ForeignKey('Section', on_delete=models.CASCADE)


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_code', 'course_text']


class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = ['section_text', 'percentage']
        labels = {
            'percentage': _('Percentage'),
        }
        help_texts = {
            'percentage': _('Your mark percentage for this section in the course.'),
        }


class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ['assignment_name', 'mark', 'total', 'percentage']
