from .models import Assignment, Course

from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView


# Create your views here.
def index(request):
    course_list = Course.objects.all()[:25]
    context = {
        'course_list': course_list,
    }
    return render(request, 'calculations/index.html', context)


class CourseCreate(CreateView):
    model = Course
    fields = ['course_name', 'course_code']

    def get_success_url(self):
        return reverse('calculations:index')


class CourseUpdate(UpdateView):
    model = Course
    fields = ['course_name', 'course_code']
    template_name_suffix = '_update_form'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super(CourseUpdate, self).get_context_data(**kwargs)
        course = Course.objects.get(pk=pk)
        context['course'] = course
        return context


class CourseDelete(DeleteView):
    model = Course

    def get_success_url(self):
        return reverse('calculations:index')


class CourseView(DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super(CourseView, self).get_context_data(**kwargs)
        course = Course.objects.get(pk=pk)
        context['assignment_list'] = Assignment.objects.filter(assignment_course=course, is_section=False)
        context['section_list'] = Assignment.objects.filter(assignment_course=course, is_section=True)
        context['course'] = course
        return context


class AssignmentCreate(CreateView):
    model = Assignment
    fields = ['assignment_name', 'is_section', 'mark',
              'total', 'percentage', 'assignment_self', 'assignment_course']

    def get_initial(self):
        pk = self.kwargs['pk']
        course = Course.objects.get(pk=pk)
        return {'assignment_course': course}

    def get_form(self, form_class=None):
        pk = self.kwargs['pk']
        course = Course.objects.get(pk=pk)

        form = super(AssignmentCreate, self).get_form(form_class)
        form.fields['assignment_self'].queryset = Assignment.objects.filter(assignment_course=course)
        return form

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        is_section = self.kwargs['is_section']
        context = super(AssignmentCreate, self).get_context_data(**kwargs)

        if is_section:
            self.model.assignment_course = Course.objects.get(pk=pk)
            is_section = 1
        else:
            self.model.assignment_self = Assignment.objects.get(pk=pk)
            is_section = 0

        context['course'] = self.model.assignment_course
        context['pk'] = pk
        context['is_section'] = is_section
        return context

    def form_valid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        form.instance.assignment_course_id = context['pk']
        form.save()
        return super(AssignmentCreate, self).form_valid(form)


class AssignmentUpdate(UpdateView):
    model = Assignment
    fields = ['assignment_name', 'is_section', 'mark',
              'total', 'percentage', 'assignment_self',
              'assignment_course']
    template_name_suffix = '_update_form'

    def get_initial(self):
        pk = self.kwargs['pk']
        course = Assignment.objects.get(pk=pk).assignment_course
        return {'assignment_course': course}

    def get_form(self, form_class=None):
        pk = self.kwargs['pk']
        course = Assignment.objects.get(pk=pk).assignment_course

        form = super(AssignmentUpdate, self).get_form(form_class)
        form.fields['assignment_self'].queryset = Assignment.objects.filter(assignment_course=course)
        return form

    def form_valid(self, form):
        form.save()
        return super(AssignmentUpdate, self).form_valid(form)


class AssignmentDelete(DeleteView):
    model = Assignment

    def get_success_url(self):
        if self.object.assignment_course is None:
            assignment = Assignment.objects.get(pk=self.object.assignment_self.pk)
            pk = assignment.assignment_course.pk
            return reverse('calculations:view_course', kwargs={'pk': pk})
        else:
            pk = self.object.assignment_course.pk
            return reverse('calculations:view_course', kwargs={'pk': pk})
