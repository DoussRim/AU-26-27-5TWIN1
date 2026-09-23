from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Hello(request):
    #return HttpResponse("Bonjour <b>5TWIN1</b>")
    return render(request,template_name='event/show.html')