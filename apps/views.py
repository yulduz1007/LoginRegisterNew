from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView

from apps.forms import RegisterForm, LoginForm, ProfileForm
from apps.models import User


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

class RegisterFormView(FormView):
    form_class = RegisterForm
    template_name = 'register-form.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



    def form_invalid(self, form):
        return super().form_invalid(form)


class CustomLogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('login')
class LoginFormView(FormView):
    form_class = LoginForm
    template_name = 'login-form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        if form.is_valid():
            user = form.find_user
            login(self.request , user)
            return super().form_valid(form)

class ProfileTemplateView(TemplateView):
    template_name = "profile.html"

class ProfileEditFormView(FormView):
    template_name = "profile-edit.html"
    success_url = reverse_lazy("profile")
    form_class = ProfileForm

    def form_valid(self, form):
        user = self.request.user
        form_data = form.cleaned_data
        form_data['first_name'] = form_data.get("fullname").split()[0]
        form_data['last_name'] = form_data.get("fullname").split()[1]
        del form_data['fullname']
        user = User.objects.filter(pk=user.pk)
        user.update(**form.cleaned_data)
        return super().form_valid(form)





