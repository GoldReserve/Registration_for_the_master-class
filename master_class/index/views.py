from django.shortcuts import render

from index.forms import MasterClassRegistration


# Create your views here.
def index(request):
    message = False
    if request.method == 'POST':
        form = MasterClassRegistration(request.POST)
        if form.is_valid():
            #Тут мы передаем form.cleaned_data в телегу
            print(form.cleaned_data)
            message = 'Вы успешно записались на мастер класс!'
    else:
        form = MasterClassRegistration()
    return render(request, 'index/index.html', {'form': form, 'message': message, 'cleaned_data':form.cleaned_data})

