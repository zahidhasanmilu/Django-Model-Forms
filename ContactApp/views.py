from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm


# Create your views here.
def home(request):
    form = ContactForm()
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponse('Contact Save Successfully')    
    context={
        'forms':form
    }
    return render(request,'index.html', context)