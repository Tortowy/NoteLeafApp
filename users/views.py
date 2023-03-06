from django.shortcuts import render,redirect

from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from .forms import RegisterForm,UserAdminChangeForm,EditUserForm,PasswordChangingForm

from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    DeleteView,
    UpdateView
)


from .models import Account

# Create your views here.

#ListView

User = get_user_model()


def emailSentView(request):
    return render(request,"registration/password_reset_done.html",{})


class UserUpdateView(UpdateView,LoginRequiredMixin):
    login_url = "/users/login_user/"

    form_class = EditUserForm

    template_name = 'users/account_edit.html'



    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Your acount was updated!")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'users/change_password.html'
    success_url = '/users/detail/'



def account_detail(request):
    user = Account.objects.get(id=request.user.id)
    context = {
        "object" : user
    }
    return render(request,"users/account_detail.html",context)



def logout_user(request):
    logout(request)
    messages.success(request,("You were logged out!"))
    return redirect('home')

def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You were logged in!"))
            return redirect('home')
        else:
            messages.error(request,("There was an error loggin in, try egain..."))
            return redirect('/users/login_user')

    else:
        return render(request,'users/login_user.html',{})

def activate(request,uidb64,token):

    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active = True
        user.save()

        messages.success(request,("Thank You for Your email confirmation, now you can log in to Your account."))
        return redirect('/users/login_user')
    else:
        messages.error(request,("Activation link is invalid!"))

    return redirect('home')


def activateEmail(request,user,to_email):
    mail_subject = "Active your account"
    message = render_to_string("users/template_activate_account.html",{

        'user'      :   user.username,
        'domain'    :   get_current_site(request).domain,
        'uid'       :   urlsafe_base64_encode(force_bytes(user.pk)),
        'token'     :   account_activation_token.make_token(user),
        'protocol'  :   'https' if request.is_secure() else 'http'
    })

    email = EmailMessage(mail_subject,message,to=[to_email])
    if email.send():
        messages.info(request, f'Dear {user.username}, please go to Your email {to_email} inbox and click on \
                received activation link to confirm your account. Note: check your spam folder.')
    else:
        messages.error(request,f'Problem sending email to {to_email}, check if you typed it correctly.')






def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request,user,form.cleaned_data.get('email'))


            #messages.success(request,("Registration succesful!"))
            return redirect('home')
        else:
            messages.error(request,("There was an error with your form..."))
    else:
        form = RegisterForm()
    return render(request,'users/register_user.html',{'form':form,})