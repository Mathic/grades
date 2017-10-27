from django.http import JsonResponse
from django.urls import reverse
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, TemplateView

from .models import Assignment, Course


# Create your views here.
class CourseMixin(object):
    def get_courses(self):
        return Course.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CourseMixin, self).get_context_data(**kwargs)
        context['courses'] = self.get_courses()
        return context


def update_assignment_list(request):
    course_selected = request.GET.get('course_selected', None)
    course = Course.objects.get(course_name=course_selected)
    print(course)
    print(assignments)
    data = {
        'assignments': assignments
    }
    if data['assignments'] is None:
        data['error_message'] = 'No assignments found'
    return JsonResponse(data)


class IndexView(CourseMixin, TemplateView):
    template_name = 'calculations/index.html'


class CourseCreate(CourseMixin, CreateView):
    model = Course
    fields = ['course_name', 'course_code']

    def get_success_url(self):
        return reverse('calculations:index')


class CourseUpdate(CourseMixin, UpdateView):
    model = Course
    fields = ['course_name', 'course_code']
    template_name_suffix = '_update_form'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super(CourseUpdate, self).get_context_data(**kwargs)
        course = Course.objects.get(pk=pk)
        context['course'] = course
        return context


class CourseDelete(CourseMixin, DeleteView):
    model = Course

    def get_success_url(self):
        return reverse('calculations:index')


class CourseView(CourseMixin, DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        context = super(CourseView, self).get_context_data(**kwargs)
        course = Course.objects.get(pk=pk)
        context['assignment_list'] = Assignment.objects.filter(assignment_course=course, is_section=False)
        context['section_list'] = Assignment.objects.filter(assignment_course=course, is_section=True)
        context['course'] = course
        return context


class AssignmentCreate(CourseMixin, CreateView):
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


class AssignmentUpdate(CourseMixin, UpdateView):
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


class AssignmentDelete(CourseMixin, DeleteView):
    model = Assignment

    def get_success_url(self):
        if self.object.assignment_course is None:
            assignment = Assignment.objects.get(pk=self.object.assignment_self.pk)
            pk = assignment.assignment_course.pk
            return reverse('calculations:view_course', kwargs={'pk': pk})
        else:
            pk = self.object.assignment_course.pk
            return reverse('calculations:view_course', kwargs={'pk': pk})
