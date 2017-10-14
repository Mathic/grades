from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator


# user: spysauce
# password: password123
# Create your models here.
class Section(models.Model):
    section_text = models.CharField(max_length=200)
    percentage = models.IntegerField(default=0,
                                     validators=[
                                         MaxValueValidator(100),
                                         MinValueValidator(1)
                                     ])
    models.ForeignKey('self')

    def __str__(self):
        return self.section_text
