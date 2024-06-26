
from django.shortcuts import render
from django.db.models import Q

from ice_cream.models import Category,IceCream

def index(request):
    template_name = 'homepage/index.html'
    # Запрос:
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'description'
        ).filter(
            Q(is_published=True) 
            & Q(is_on_main=True) 
            | Q(title__contains='пломбир')
            & Q(is_published=True)
        )
    # Полученный из БД QuerySet передаём в словарь контекста:
    context = {
        'ice_cream_list': ice_cream_list,
    }
    # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
    return render(request, template_name, context)