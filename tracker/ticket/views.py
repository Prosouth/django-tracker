from django.shortcuts import render_to_response
from django.http import HttpResponse
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
