from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView

from account_module.models import User
from user_panel_module.forms import EditProfileForm, EditPasswordForm


# Create your views here.

@method_decorator(login_required,'dispatch')
class UserPanelView(TemplateView):
    template_name = 'user_panel_module/user_panel_page.html'


@method_decorator(login_required,'dispatch')
class EditUserProfile(View):
    def get(self, request: HttpRequest):
        user = User.objects.filter(id=request.user.id).first()
        form = EditProfileForm(instance=user)
        context = {
            'user': user,
            'form': form
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)

    def post(self, request: HttpRequest):
        user = User.objects.filter(id=request.user.id).first()
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
        context = {
            'user': user,
            'form': form
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)


@method_decorator(login_required,'dispatch')
class EditPasswordView(View):
    def get(self, request: HttpRequest):
        request.user.is_authenticated
        form = EditPasswordForm()
        context = {
            'form': form
        }
        return render(request, 'user_panel_module/edit_password_page.html', context)

    def post(self, request: HttpRequest):
        form = EditPasswordForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(id=request.user.id).first()
            current_password = form.cleaned_data.get('current_password')
            new_password = form.cleaned_data.get('new_password')
            confirm_new_password = form.cleaned_data.get('confirm_new_password')
            if user.check_password(current_password):
                if new_password.isdigit():
                    form.add_error('new_password', 'رمز عبور شما نمی تواند کلا عدد باشد')
                else:
                    if new_password.isalpha():
                        form.add_error('new_password', 'رمز عبور شما نمی تواند کلا حروف باشد')
                    else:
                        if new_password != confirm_new_password:
                            form.add_error('confirm_new_password', 'رمز عبور با تکرار رمز عبور تفاوت دارد')
                        else:
                            user.set_password(new_password)
                            user.save()
                            logout(request)
                            return redirect('account_login')

            else:
                form.add_error('current_password',  'رمز عبور شما اشتباه است')
        context = {
            'form': form
        }
        return render(request, 'user_panel_module/edit_password_page.html', context)
