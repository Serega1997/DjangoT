from django.shortcuts import render
from .services.service import *


def index(request):
    condition = ''
    text = ''
    text_caesar_choice = ''
    text_caesar_decryption = ''

    if request.method == 'POST':
        condition = request.POST['radiobutton']
        text = request.POST['text']

        for shift in range(1, len(language(condition)) + 1):
            text_caesar_choice += f'<p>ROT{shift}&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;{caesar_choice(text, language(condition), shift)} </p><br> '

    context = {
        'condition': condition,
        'text': text,
        'text_Caesar_choice': text_caesar_choice
    }
    return render(request, 'Caesar/Главная.html', context)
