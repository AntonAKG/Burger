from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import login


from account.forms import LoginForm, RegisterForm, UserProfileForm
from cart.models import Cart

User = get_user_model()


class LoginClassView(View):

    template_name = "registration/login.html"
    authentication_form = LoginForm

    success_url = reverse_lazy("main_index")

    def form_valid(self, form):
        response = super().form_valid(form)

        # Get the session key and transfer the cart items to the user
        session_key = self.request.session.session_key
        print("]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
        print(session_key)

        if session_key:
            carts = Cart.objects.filter(session_key=session_key)
            print(carts)
            for cart in carts:
                cart.user = self.request.user
                cart.session_key = None
                cart.save()

        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Sign in"

        return context


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        response = super().form_valid(form)

        # Get the session key and transfer the cart items to the user
        session_key = self.request.session.session_key
        if session_key:
            carts = Cart.objects.filter(session_key=session_key)
            for cart in carts:
                cart.user = self.request.user
                cart.session_key = None
                cart.save()

        # Log in the user after registration
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        user = authenticate(self.request, email=email, password=password)
        if user:
            login(self.request, user)

        return response


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "account/profile.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["title"] = "Profile"
        context["form"] = UserProfileForm(instance=self.request.user)
        return context

    @staticmethod
    def post(request: object) -> object:
        form = UserProfileForm(request.POST, instance=request.user, files=request.FILES)

        if form.is_valid():

            email = form.cleaned_data["email"]
            if User.objects.filter(email=email).exists():
                form.save()
                form.add_error(
                    "email", "Користувач з такою адресою електронної пошти вже існує."
                )
            else:

                form.save()
                return redirect("profile")

        return render(request, "account/profile.html", {"form": form})


class UserCart(TemplateView):
    template_name = "account/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Cart"
        return context
