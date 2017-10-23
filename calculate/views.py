from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from .models import Assignment, Course, Section


# Create your views here.
def index(request):
    course_list = Course.objects.all()[:25]
    context = {
        'course_list': course_list,
    }
    return render(request, 'calculate/index.html', context)


class CourseDetail(DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super(CourseDetail, self).get_context_data(**kwargs)
        course = Course.objects.get(pk=pk)
        context['section_list'] = Section.objects.filter(section_course=course)
        context['course'] = course
        return context


class CourseCreate(CreateView):
    model = Course
    fields = ['course_code', 'course_text', 'atype']

    def get_success_url(self):
        return reverse('calculate:course_detail', args=[self.object.id])


class CourseUpdate(UpdateView):
    model = Course
    fields = ['course_code', 'course_text']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('calculate:course_detail', args=[self.object.id])


class CourseDelete(DeleteView):
    model = Course

    def get_success_url(self):
        return reverse('calculate:index')


class SectionDetail(DetailView):
    model = Section

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super(SectionDetail, self).get_context_data(**kwargs)
        section = Section.objects.get(pk=pk)
        context['section_list'] = Section.objects.filter(section_section=section)
        context['assignment_list'] = Assignment.objects.filter(assignment_section=section)
        context['section'] = section
        return context


class SectionCreate(CreateView):
    model = Section
    fields = ['section_text', 'percentage', 'section_section', 'section_course']

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        s_type = self.kwargs['s_type']
        context = super(SectionCreate, self).get_context_data(**kwargs)

        is_greater_than_100 = False
        if s_type == 'Course':
            course = Course.objects.get(pk=pk)
            self.model.section_course = course

            # percentage logic
            section_list = Section.objects.filter(section_course=course)
            total = 0
            for section in section_list:
                total += section.percentage

            if total > 100:
                is_greater_than_100 = True
            else:
                is_greater_than_100 = False

        if s_type == 'Section':
            s = Section.objects.get(pk=pk)
            section.section_section = s

        context['course'] = course
        context['pk'] = pk
        context['s_type'] = s_type
        context['is_greater_than_100'] = is_greater_than_100
        return context

    def form_valid(self, form):
        form.save()
        return super(SectionCreate, self).form_valid(form)


class SectionUpdate(UpdateView):
    model = Section
    fields = ['section_text', 'percentage', 'section_section', 'section_course']
    template_name_suffix = '_update_form'


class SectionDelete(DeleteView):
    model = Section

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super(SectionDelete, self).get_context_data(**kwargs)
        context['pk'] = pk
        return context

    def get_success_url(self):
        return reverse('calculate:index')


class AssignmentDetail(DetailView):
    model = Assignment


class AssignmentCreate(CreateView):
    model = Assignment
    fields = ['assignment_name', 'mark', 'total', 'percentage']

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super(AssignmentCreate, self).get_context_data(**kwargs)
        s = Section.objects.get(pk=pk)
        self.model.assignment_section = s
        context['pk'] = pk
        return context

    def form_valid(self, form):
        form.save()
        return super(AssignmentCreate, self).form_valid(form)


class AssignmentUpdate(UpdateView):
    model = Assignment
    fields = ['assignment_name', 'mark', 'total', 'percentage', 'assignment_section']
    template_name_suffix = '_update_form'


class AssignmentDelete(DeleteView):
    model = Assignment

    def get_success_url(self):
        return reverse('calculate:index')
