from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, get_list_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

import users.admin
from languages.models import Languages
from .forms import AddLanguage


def select_language(request):
    if request.method == 'POST':
        form = Languages(request.POST)
    else:
        form = Languages()
    return render(request, 'languages/select_language.html', {'form': form})


class MyView(LoginRequiredMixin, View):
    login_url = '/users/login/'
    redirect_field_name = '/users/login/'


class AddLanguage(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Languages
    fields = ['name']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super(AddLanguage, self).form_valid(form)


class UpdateLanguage(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Languages
    fields = ['name']


class DeleteLanguage(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Languages
    success_url = reverse_lazy('language_default')

    def get_object(self):
        user_id_ = self.kwargs.get("user_id")
        return get_object_or_404(Languages, user_id=user_id_)



def get_language(reguest, pk: int):
    languages_list = get_list_or_404(Languages, user_id=pk)
    return render(reguest, 'languages/select_language.html', {'languages_list': languages_list})


class LinksView(ListView):
    model = Languages
    template_name = 'languages/select_language.html'
    context_object_name = 'links'

    def get_queryset(self):
        return Languages.objects.filter(user=10)


def language_default(request):
    languages_list = Languages.objects.filter(user=request.user)
    return render(request, 'languages/select_language.html', {'languages_list': languages_list})


def my_view(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.id
        # form = Languages()
        print(type(username))
        vid = get_object_or_404(Languages, user_id=username)
        #var = request.session.get('lang', 'asd')
        request.session['lang'] = vid.name
        request.session.modified = True
        #print(request.POST)
        # print(form.cleaned_data)
        #print(username)
        #print(vid)

    return render(request, 'languages/select_language.html', {'languages_list': vid})
