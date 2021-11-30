from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .forms import PasswordChangingForm, RegistrationForm, EditProfileForm
from blogfeed.models import Profile


class ShowProfilePage(DetailView):
    model = Profile
    template_name = 'profile_page.html'

    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()
        context = super(ShowProfilePage, self).get_context_data(
            *args, **kwargs)
        profile_view_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["user_profile"] = profile_view_user
        return context


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'profile_settings/change_password.html'
    success_url = reverse_lazy('password_success')


class UserRegisterView(generic.CreateView):
    form_class = RegistrationForm
    template_name = 'authentification/register.html'
    success_url = reverse_lazy('login')


class UserProfileView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'profile_settings/profile_edit.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


def password_success(request):
    return render(request, 'password_success.html', {})
