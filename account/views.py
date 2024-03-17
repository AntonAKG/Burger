from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from account.forms import LoginForm, RegisterForm, UserProfileForm

User = get_user_model()


class LoginClassView(LoginView):
    template_name = 'registration/login.html'
    LoginView.authentication_form = LoginForm

    success_url = reverse_lazy('main_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Sign in'

        return context


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super(RegisterView, self).form_valid(form)

        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')

        user = authenticate(self.request, email=email, password=password)

        if user:
            user.set_password(password)
            user.save()

        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'account/profile.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['title'] = 'Profile'
        context['form'] = UserProfileForm(instance=self.request.user)
        return context

    @staticmethod
    def post(request: object) -> object:
        form = UserProfileForm(request.POST, instance=request.user, files=request.FILES)

        if form.is_valid():

            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                form.save()
                form.add_error('email', 'Користувач з такою адресою електронної пошти вже існує.')
            else:

                form.save()
                return redirect('profile')

        return render(request, 'account/profile.html', {'form': form})
