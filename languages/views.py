from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from languages.models import Languages


class AddLanguage(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Languages
    fields = ['name']
    success_url = reverse_lazy('list_languages')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super(AddLanguage, self).form_valid(form)


class DeleteLanguage(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Languages
    success_url = reverse_lazy('list_languages')


def get_language(request, pk: int):
    request.session['language'] = pk
    request.session.modified = True
    return redirect('../../video_youtube/list_videos/')


class LanguagesListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    template_name = 'languages/languages_list.html'

    def get_queryset(self):
        # count_word = Languages.objects.raw('select l.name, count(n.*) from languages l left join new_words n on n.language_id=l.id group by 1')
        # print(count_word)
        # https://docs.djangoproject.com/en/4.0/topics/db/aggregation/
        # https://django.fun/docs/django/ru/4.0/ref/models/querysets/#extra
        return Languages.objects.filter(user_id=self.request.user.id)

