from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View

from contact_us_module.models import ContactUs


# Create your views here.


@method_decorator(login_required,'dispatch')
class ContactUsView(View):
    def get(self,request:HttpRequest):
        return render(request,'contact_us_module/contact_us_page.html')

    def post(self,request:HttpRequest):
        message=request.POST.get('message')
        new_contact=ContactUs(user_name=request.user.username,email=request.user.email,message=message)
        new_contact.save()
        return redirect('home_page')