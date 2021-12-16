from django.shortcuts import render
from .models import categories_db


def index(request):
    links = ''
    for i in categories_db:
        if i['condition'] == '1':
            links += f'<a href="{i["link"]}">{i["name"]}</a><br>'
        else:
            links += f'<p class=text">{i["name"]}</p><br>'

    context = {
        'links': links,
    }
    return render(request, 'homepage/home.html', context)
