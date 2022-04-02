from django.conf.global_settings import LANGUAGES
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, get_list_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from new_words.models import NewWords
import users.admin
from languages.models import Languages
from .forms import AddLanguageForm

from django.db.models import Count


def select_language(request):
    if request.method == 'POST':
        form = AddLanguageForm(request.POST)
        print("fffffffffffff222222222222222")
    else:
        form = AddLanguageForm().name
        print("fffffffffffff1111111111111111")
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
    success_url = reverse_lazy('select_language')
    # lang_full_name = [l[1] for l in LANGUAGES if l[0] == 'uz']
    # lang_full_name = "sdfsdfsef"
    # extra_context = {'lang_full_name': lang_full_name}
    # template_name = 'lang_delete.html'
    # pk_url_kwarg = 'pk'

    # def form_valid(self, form):
    #    form.instance.user_id = self.request.user.id
    #    return super(DeleteLanguage, self).form_valid(form)

    # def get_object(self):
    #    user_id_ = self.kwargs.get("user_id")
    #    return get_object_or_404(Languages, user_id=user_id_)


def get_language(request, pk: int):
    request.session['language'] = pk
    request.session.modified = True
    return redirect('../../video_youtube/list_video/')


class GetCountWords:
    new_word_count = 0

    def __init__(self):
        GetCountWords.new_word_count = NewWords.objects.count()

    def get_list_languages(self):
        list_languages = Languages.objects.all()
        return list_languages.id

    def get_count_new_word(self):
        list_languages = Languages.objects.all()
        new_word_count = NewWords.objects.filter(user_id=1).count()
        return new_word_count
        # GetCountWords.new_word_count = Languages.objects.filter(user_id=1).count()

    def get_count_learned_word(self):
        pass


class LanguagesListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    #model = Languages
    template_name = 'languages/select_language.html'
    # q1=Languages.objects.all()
    # q2=NewWords.objects.all()

    # lang_full_name = [l[1] for l in LANGUAGES if l[0] == 'uz']
    extra_context = {'lang_full_name': GetCountWords.new_word_count}

    # quryset = Languages.objects.filter(user_id=self.request.user.id)

    # request.session['username1'] = 'qwe'
    # request.session.modified = True
    def get_queryset(self):
        count_word = Languages.objects.filter(user_id=self.request.user.id)

        #https://docs.djangoproject.com/en/4.0/topics/db/aggregation/
        return count_word



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
        # var = request.session.get('lang', 'asd')
        request.session['lang'] = vid.name
        request.session.modified = True
        # print(request.POST)
        # print(form.cleaned_data)
        # print(username)
        # print(vid)

    return render(request, 'languages/select_language.html', {'languages_list': vid})
