from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_code = models.CharField(max_length=8, unique=True)

    def get_absolute_url(self):
        return reverse('calculations:view_course', kwargs={'pk': self.pk})

    def __str__(self):
        return self.course_name


class Assignment(models.Model):
    assignment_name = models.CharField(max_length=50)
    is_section = models.BooleanField(default=False)
    mark = models.IntegerField(default=0)
    total = models.IntegerField(default=100)
    percentage = models.IntegerField(default=0,
                                     validators=[
                                         MaxValueValidator(100),
                                         MinValueValidator(1)
                                     ])
    assignment_self = models.ForeignKey('self',
                                        null=True,
                                        blank=True,
                                        limit_choices_to={'is_section': True},
                                        verbose_name='Assignment',
                                        on_delete=models.CASCADE)
    assignment_course = models.ForeignKey('Course',
                                          blank=True,
                                          on_delete=models.CASCADE)

    def get_absolute_url(self):
        if self.assignment_course is None and self.assignment_self is None:
            return reverse('calculations:index')
        if self.assignment_course is None:
            assignment = Assignment.objects.get(pk=self.assignment_self.pk)
            course = assignment.assignment_course
            return reverse('calculations:view_course', kwargs={'pk': course.pk})
        else:
            return reverse('calculations:view_course', kwargs={'pk': self.assignment_course.pk})

    def __str__(self):
        return self.assignment_name
