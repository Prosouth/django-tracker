from django.shortcuts import render_to_response
from django.http import HttpResponse
from datetime import date, timedelta
from models import Task


# Create your views here.
def home(request, name=None):
    if name:
        return HttpResponse("Hello %s!" % name)
    else:
        return HttpResponse("Hello world!")


def ticket_listing(request):
    objets = Task.objects.all().order_by('-due_date')
    return render_to_response('ticket/list.html', {'objets': objets})


def ticket_detail(request, id):
    objet = Task.objects.get(pk=id)
    return render_to_response('ticket/detail.html', {'objet': objet})


def ticket_list(request, filter):
    if filter == 'closed':
        objets = Task.objects.filter(closed=True)
    elif filter == 'open':
        objets = Task.objects.filter(closed=False)
    elif filter == 'week':
        objets = Task.objects.filter(
            due_date__lte=date.today() + timedelta(days=7)).filter(
                due_date__gte=date.today())
        return render_to_response('ticket/list.html', {'objets': objets})
