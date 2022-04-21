from django.shortcuts import render


def index(request):
    context = {
        'title':'Последние обновления на сайте',
        'tag':'Главная страница',
        'cout':5,
        'temp':[1,2,3,4,5]
    }
    return render(request, 'mysite/index.html', context)


def group_list(request):
    context = {
        'title': 'Лев Толстой – зеркало русской революции',
        'tag':'Лев Толстой'
    }
    return render(request, 'mysite/group_list.html', context)


def about(request):
    context = {
        'title':'немного про нас:',
        'tag':'о нас'
    }
    return render(request, 'mysite/about.html', context)


def register(request):
    context = {
        'title':'регистрация'
    }
    return render(request, 'mysite/register.html', context)