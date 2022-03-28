from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect

from users.forms import UserCreationForm


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        content = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, content)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            print(request.POST)
            print(form.cleaned_data)
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('../../languages/add_language/')
        content = {
            'form': form
        }
        return render(request, self.template_name, content)
