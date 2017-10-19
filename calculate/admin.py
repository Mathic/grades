from django.contrib import admin
from .models import Assignment, Course, Section

# Register your models here.
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Assignment)
