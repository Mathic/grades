from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

from .models import Section, SectionForm


# Create your views here.
def index(request):
    section_list = Section.objects.all()[:25]
    context = {
        'section_list': section_list,
    }
    return render(request, 'calculate/index.html', context)


def detail(request, section_id):
    try:
        section = Section.objects.get(pk=section_id)
    except Section.DoesNotExist:
        raise Http404("Section does not exist")
    return render(request, 'calculate/detail.html', {'section': section})


def add(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/calculate')
    else:
        form = SectionForm()
    return render(request, 'calculate/add.html', {'form': form})
