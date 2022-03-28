from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model

import users.admin
from languages.models import Languages
from .forms import AddLanguage


def select_language(request):
    if request.method == 'post':
        form = Languages(request.POST)
    else:
        form = Languages()
    return render(request, 'languages/select_language.html', {'form': form})


def add_language(request):
    form = AddLanguage(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        # form = AddLanguage(request.POST)
        # if form.is_valid():
        try:
            language = form.save(commit=False)
            language.name = language.name
            language.user_id = request.user.id
            language.save()
            print(request.POST)
            print(form.cleaned_data)
        except Exception:
            pass

    # else:
    # form = AddLanguage()
    return render(request, 'languages/add_language.html', {'form': form})


def get_language(reguest, pk: int):
    languages_list = get_list_or_404(Languages, user_id=pk)
    return render(reguest, 'languages/select_language.html', {'languages_list': languages_list})
