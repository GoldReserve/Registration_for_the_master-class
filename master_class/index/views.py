from django.shortcuts import render

from index.forms import MasterClassRegistration
from telegram_bot import send_message


# Create your views here.
def index(request):

    message = 'Вы успешно записались на мастер класс!'

    if request.method == 'POST':
        form = MasterClassRegistration(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

            # Тут мы передаем form.cleaned_data в телегу
            send_message(data=form.cleaned_data)

    else:
        form = MasterClassRegistration()
    try:
        return render(request, 'index/index.html', {'form': form, 'message': message,
                                                    'cleaned_data': form.cleaned_data})
    except AttributeError:
        return render(request, 'index/index.html', {'form': form})

