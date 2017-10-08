from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View


class Registraton(View):
    def get(self, request):
        return render(request, 'index.html', {'form': RegistrationForm(),
                                              'errors': []})


class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=5, label='Логин')
    password = forms.CharField(min_length=6, widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(min_length=6, widget=forms.PasswordInput, label='Повторите пароль')


def singup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            password = request.POST.get('password', None)
            password2 = request.POST.get('password2', None)
            if password == password2 and password is not None:
                return HttpResponseRedirect('/login')
            else:
                return render(request, 'index.html', {'form': form,
                                                      'errors': ["Пароли не совпадают"]})
        else:
            form = RegistrationForm()
        return render(request, 'index.html', {'form': form})
    else:
        return HttpResponseRedirect('/')
        #     username = request.POST.get('username', None)
        #     if not login:
        #         errors.append('Не указан логин')
        #     elif len(username) < 5:
        #         errors.append('Логин состоит менее чем из 5 символов')
        #
        #     if not password:
        #         errors.append('Не указан пароль')
        #     elif len(password) < 6:
        #         errors.append('Пароль состоит менне чем из 6 символов')
        #
        #     if not password2:
        #         errors.append('Не указано подтверждение пароля')
        #
        #     if password != password2:
        #         errors.append('Пароли не совпадают')
        #
        #     if not errors:
        #         return HttpResponseRedirect('/login')
        # return render(request, 'index.html', {'errors': errors})


def login(request):
    return render(request, 'form.html')
