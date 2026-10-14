from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.urls import reverse_lazy
from .forms import EventForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def Hello(request):
    #return HttpResponse("Bonjour <b>5TWIN1</b>")
    return render(request,template_name='event/show.html')
@login_required(login_url='log')
def Event_List(request):
    liste=Event.objects.all()#Queyset
    return render(request,'event/liste.html',
                  {'ll':liste})
class Affiche_Event(LoginRequiredMixin,ListView):
    model=Event
    # template_name="event/liste.html"
    context_object_name="ll"
    ordering=['-evt_date']
class Details(DetailView):
    model=Event
    template_name="event/details.html"
    # context_object_name="evt"
class Supp(DeleteView):
    model=Event
class Update(UpdateView):
    model=Event
    form_class=EventForm
    success_url=reverse_lazy('Gen_list')
class Ajout(CreateView):
    model=Event
    form_class=EventForm
    success_url=reverse_lazy('Gen_list')
    
    
   
    