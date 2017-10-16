from django.shortcuts import render
from django.http import Http404

from .models import Section


# Create your views here.
def index(request):
    section_list = Section.objects.all()[:5]
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
    return render(request, 'calculate/add.html')
