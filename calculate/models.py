from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


# user: spysauce
# password: password123
# Create your models here.
class Course(models.Model):
    DEFAULT_PK = 1
    course_name = models.CharField(max_length=50)
    course_code = models.CharField(max_length=8, unique=True)
    atype = models.CharField(max_length=10, default='Course')

    def get_absolute_url(self):
        return reverse('calculate:course_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.course_name


class Section(models.Model):
    section_name = models.CharField(max_length=50)
    percentage = models.IntegerField(default=100,
                                     validators=[
                                         MaxValueValidator(100),
                                         MinValueValidator(1)
                                     ])
    atype = models.CharField(max_length=10, default='Section')
    section_section = models.ForeignKey('self',
                                        blank=True,
                                        null=True,
                                        on_delete=models.CASCADE)
    section_course = models.ForeignKey('Course',
                                       blank=True,
                                       null=True,
                                       default=Course.DEFAULT_PK,
                                       on_delete=models.CASCADE)

    def get_absolute_url(self):
        if self.section_course is None:
            pk = self.section_section.pk
        else:
            pk = self.section_course.pk
        return reverse('calculate:course_detail', kwargs={'pk': pk})

    def __str__(self):
        return self.section_name


class Assignment(models.Model):
    assignment_name = models.CharField(max_length=50)
    mark = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    percentage = models.IntegerField(default=0,
                                     validators=[
                                         MaxValueValidator(100),
                                         MinValueValidator(1)
                                     ])
    assignment_section = models.ForeignKey('Section',
                                           on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('calculate:assignment_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.assignment_name
