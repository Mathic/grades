from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


# user: spysauce
# password: password123
# Create your models here.
class Course(models.Model):
    course_code = models.CharField(max_length=8, default='PHYS1001')
    course_text = models.CharField(max_length=50)
    atype = models.CharField(max_length=10, default='Course')

    def __str__(self):
        return self.course_text


class Section(models.Model):
    section_text = models.CharField(max_length=50)
    percentage = models.IntegerField(default=0,
                                     validators=[
                                         MaxValueValidator(100),
                                         MinValueValidator(1)
                                     ])
    atype = models.CharField(max_length=10, default='Section')
    section_section = models.ForeignKey('self',
                                        null=True,
                                        blank=True,
                                        on_delete=models.CASCADE)
    section_course = models.ForeignKey('Course',
                                       null=True,
                                       blank=True,
                                       on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('calculate:section_detail', kwargs={'pk': self.pk})

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
    assignment_section = models.ForeignKey('Section',
                                           on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('calculate:assignment_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.assignment_name
