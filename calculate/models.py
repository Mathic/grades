from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _


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
