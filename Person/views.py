from django.shortcuts import render,redirect
from .forms import FormRegistration
from django.contrib.auth import login
# Create your views here.
def SignUp(request):
    if request.method=="POST":
        form=FormRegistration(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('aff')
            # return redirect('log')
    else:
        form=FormRegistration()
    return render(request,template_name="registration/SignUp.html",
                  context={'ff':form})
            
            