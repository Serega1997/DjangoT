def language(selected):  # функция выбора алфавита
    language_ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    language_en = 'abcdefghijklmnopqrstuvwxyz'

    if selected == 'ru':
        selected_language = language_ru
    elif selected == 'en':
        selected_language = language_en

    return selected_language


def caesar_choice(text, selected_language, shift):  # шифрование Цезаря
    new_text = ''
    for i in text:
        if i.lower() in selected_language:
            if i.upper() == i:
                new_text += selected_language[(selected_language.index(i.lower()) + shift) % len(selected_language)].upper()
            else:
                new_text += selected_language[(selected_language.index(i) + shift) % len(selected_language)]
        else:
            new_text += i
    return new_text


def caesar_decryption(text, selected_language, shift):  # дешифровка
    new_text = ''
    for i in text:
        if i.lower() in selected_language:
            if i.upper() == i:
                new_text += selected_language[(selected_language.index(i.lower()) - shift) % len(selected_language)].upper()
            else:
                new_text += selected_language[(selected_language.index(i) - shift) % len(selected_language)]
        else:
            new_text += i
    return new_text
