from .models import Assignment, Course, Section
from .forms import AssignmentForm, CourseForm, SectionForm

from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DeleteView
from django.urls import reverse


# Create your views here.
def index(request):
    course_list = Course.objects.all()[:25]
    context = {
        'course_list': course_list,
    }
    return render(request, 'calculate/index.html', context)


def course_details(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        raise Http404("Course does not exist")

    section_list = Section.objects.filter(course_fk=course)
    context = {
        'section_list': section_list,
        'course': course,
    }
    return render(request, 'calculate/course_details.html', context)


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

    assignment_list = Assignment.objects.filter(assignment_section=section)
    section_list = Section.objects.filter(section_fk=section)

    context = {
        'assignment_list': assignment_list,
        'section_list': section_list,
        'section': section,
    }
    return render(request, 'calculate/section_details.html', context)


def add_section(request, s_type, pk):
    context = {
        's_type': s_type,
        'pk': pk,
    }

    if request.method == 'POST':
        section_form = SectionForm(request.POST)
        section = section_form.save(commit=False)
        if s_type == 'Course':
            c = Course.objects.get(pk=pk)
            section.course_fk = c
        if s_type == 'Section':
            s = Section.objects.get(pk=pk)
            section.section_fk = s

        if section_form.is_valid():
            section_form.save()
            return HttpResponseRedirect('/calculate')
        else:
            raise Http404()

    return render(request, 'calculate/add_section.html', context)


class SectionDelete(DeleteView):
    model = Section

    def get_success_url(self):
        return reverse('calculate:index')


def assignment_details(request, assignment_id):
    try:
        assignment = Assignment.objects.get(pk=assignment_id)
    except Assignment.DoesNotExist:
        raise Http404("Assignment does not exist")

    context = {
        'assignment': assignment,
    }
    return render(request, 'calculate/assignment_details.html', context)


def add_assignment(request, pk):
    context = {
        'pk': pk,
    }

    if request.method == 'POST':
        assignment_form = AssignmentForm(request.POST)
        assignment = assignment_form.save(commit=False)
        s = Section.objects.get(pk=pk)
        assignment.assignment_section = s

        if assignment_form.is_valid():
            assignment_form.save()
            return HttpResponseRedirect('/calculate')
        else:
            raise Http404()

    return render(request, 'calculate/add_assignment.html', context)


class AssignmentDelete(DeleteView):
    model = Assignment

    def get_success_url(self):
        return reverse('calculate:index')
