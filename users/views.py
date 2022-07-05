from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.views.generic import UpdateView

from . import forms
from .forms import RegisterForm
from .models import Profile, CustomUser


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})


def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.email}! You have been logged in'
                return redirect('/index/')
            else:
                userlog = CustomUser.objects.get(email=form.cleaned_data['email'])
                if not userlog.is_active:
                    message = 'Sign in to your email to verify your account'
                    return render(request, 'users/login.html', context={'form': form, 'message': message})
                message = 'Login failed!'
    return render(request, 'users/login.html', context={'form': form, 'message': message})


def get_profile(request):
    if Profile.objects.filter(user__email=request.user.email).exists():
        user_profile = Profile.objects.get(user__email=request.user.email)
        context = {'user_profile': user_profile}
        return render(request, 'users/profile.html', context)
    return render(request, 'users/profile.html')


class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['name', 'age']
    success_url = '/profile/'
