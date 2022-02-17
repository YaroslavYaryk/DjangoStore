from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import LoginUserForm, RegisterUserForm
from store.utils import DataMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.list import ListView


# Create your views here.


class RegisterUser(DataMixin, SuccessMessageMixin, CreateView):
    """Show register form"""

    form_class = RegisterUserForm
    template_name = 'market/register.html'
    success_url = reverse_lazy("send_message_to_user")
    success_message = "User added successfully"
    error_message = "Registration error"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        c_def = self.get_user_context(
            title="Registration", ico="menu/img/ico/home_pink.png")
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, SuccessMessageMixin, LoginView):

    """Autorization class"""

    form_class = LoginUserForm
    template_name = 'market/sign_in.html'
    error_message = "Something went wrong"
    success_url = reverse_lazy("home")
    user = ""
    success_message = f"Successfully sign in"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        c_def = self.get_user_context(
            title="Sign in", ico="menu/img/ico/home_pink.png")

        return dict(list(context.items()) + list(c_def.items()))


class LogoutUser(LogoutView, SuccessMessageMixin):

    next_page = "home"
    success_message = "Logout successfully"


class ProfileView(DataMixin, ListView):

    model = settings.AUTH_USER_MODEL
    template_name = "market/profile.html"

    def get_context_data(self, *args, **kwargs):
        try:
            user = self.request.user
        except:
            user = None
        context = super().get_context_data(*args, **kwargs)
        c_def = self.get_user_context(
            user=user,
            title="Profile",

        )
        return dict(list(context.items()) + list(c_def.items()))
