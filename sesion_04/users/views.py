"""Users app views"""

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy

from .forms import SignupForm

# Class bases views


class LoginView(auth_views.LoginView):
    """Authenticates a user"""
    template_name = 'users/login.html'
    redirect_authenticated_user = True


class SignupView(FormView):
    """Registers a user"""
    form_class = SignupForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('users:success')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LogoutView(auth_views.LogoutView):
    """Logs out a user"""


class SuccessView(LoginRequiredMixin, TemplateView):
    """Success view"""
    template_name = 'users/success.html'


# Function based views

def sign_in(request):
    """Authenticates users"""
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('users:success')
        context['error'] = 'Credenciales incorrectas'
    return render(request, 'users/login.html', context)


def signup(request):
    """Creates a new user"""
    form = None
    if request.method == 'GET':
        form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('users:success')
    return render(request, 'users/signup.html', {'form': form})


def sign_out(request):
    """Logs out a user"""
    logout(request)
    return redirect('users:login')


@login_required
def success(request):
    """User could enter to our app"""
    return render(request, 'users/success.html')
