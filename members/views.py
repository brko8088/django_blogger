from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from .forms import PasswordChangingForm, RegistrationForm, EditProfileSettingsForm, ProfileCreationPageForm
from blogfeed.models import Profile


class ShowProfilePage(DetailView):
    model = Profile
    template_name = 'profile_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePage, self).get_context_data(
            *args, **kwargs)
        profile_view_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["user_profile"] = profile_view_user
        return context


class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfileCreationPageForm
    template_name = 'profile_settings/profile_page_creation.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePageView(UpdateView):
    model = Profile
    template_name = 'profile_settings/profile_page_edit.html'
    fields = ['bio', 'profile_picture', 'website_url', 'facebook_url',
              'instagram_url', 'twitter_url', 'github_url']
    success_url = reverse_lazy('home')


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'profile_settings/change_password.html'
    success_url = reverse_lazy('password_success')


class UserRegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserProfileSettingsView(UpdateView):
    form_class = EditProfileSettingsForm
    template_name = 'profile_settings/profile_settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


def password_success(request):
    return render(request, 'password_success.html', {})
