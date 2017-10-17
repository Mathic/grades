from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DeleteView
from django.urls import reverse

from .models import Section, SectionForm, Course, CourseForm


# Create your views here.
def index(request):
    course_list = Course.objects.all()[:25]
    section_list = Section.objects.all()[:25]
    context = {
        'section_list': section_list,
        'course_list': course_list,
    }
    return render(request, 'calculate/index.html', context)


def course_details(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        raise Http404("Course does not exist")
    return render(request, 'calculate/course_details.html', {'course': course})


def add_course(request):
    if request.method == 'POST':
        course_form = CourseForm(request.POST)
        if course_form.is_valid():
            course_form.save()
            return HttpResponseRedirect('/calculate')
    else:
        course_form = SectionForm()
    return render(request, 'calculate/add_course.html', {'course_form': course_form})


class CourseDelete(DeleteView):
    model = Course

    def get_success_url(self):
        return reverse('calculate:index')


def section_details(request, section_id):
    try:
        section = Section.objects.get(pk=section_id)
    except Section.DoesNotExist:
        raise Http404("Section does not exist")
    return render(request, 'calculate/section_details.html', {'section': section})


def add_section(request):
    if request.method == 'POST':
        section_form = SectionForm(request.POST)
        if section_form.is_valid():

            section_form.save()
            return HttpResponseRedirect('/calculate')
    else:
        section_form = SectionForm()
    return render(request, 'calculate/add_section.html', {'section_form': section_form})


class SectionDelete(DeleteView):
    model = Section

    def get_success_url(self):
        return reverse('calculate:index')
