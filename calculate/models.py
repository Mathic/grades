from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# user: spysauce
# password: password123
# Create your models here.
class Course(models.Model):
    course_code = models.CharField(max_length=8, default='PHYS1001')
    course_text = models.CharField(max_length=50)
    type = models.CharField(max_length=10, default='Course')

    def __str__(self):
        return self.course_text


class Section(models.Model):
    section_text = models.CharField(max_length=50)
    percentage = models.IntegerField(default=0,
                                     validators=[
                                         MaxValueValidator(100),
                                         MinValueValidator(1)
                                     ])
    type = models.CharField(max_length=10, default='Section')
    section_fk = models.ForeignKey('self', null=True, blank=True, related_name='section', on_delete=models.CASCADE)
    course_fk = models.ForeignKey('Course', related_name='course', on_delete=models.CASCADE, default='0')

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
