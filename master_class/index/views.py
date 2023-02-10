from django.shortcuts import render

from index.forms import MasterClassRegistration


# Create your views here.
def index(request):
    form = MasterClassRegistration()
    return render(request, 'index/index.html', {'form' : form})
