from django.shortcuts import render

# Create your views here.

from cmsPut.models import Page
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def default(request):
    if request.method == "GET":
        toReturn = "I have this pages:"
        for page in Page.objects.all():
            toReturn += "</br> <a href=/" + page.name + ">" + page.name + "</a>"
        return HttpResponse(toReturn)

@csrf_exempt
def handlePage(request, rec):
    if request.method == "GET":
        try:
            page = Page.objects.get(name=rec)
            return HttpResponse(page.body)
        except ObjectDoesNotExist:
            return HttpResponse("Content not found", status=404)
    elif request.method == "PUT" or request.method == "POST":
        page = Page(name=rec, body=request.body)
        page.save()
        return HttpResponse("Succesfully added page: " + rec)
    else:
        return HttpResponse("Method not allowed", status=405)
