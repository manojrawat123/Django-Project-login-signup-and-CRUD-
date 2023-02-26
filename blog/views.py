from django.shortcuts import render, HttpResponseRedirect
from blog.forms import SignUpForm, LoginForm, AuthorForm, ContactForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from blog.models import Blogpost
from django.contrib.auth.models import Group, User
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def home_page(request):
    userpost =  Blogpost.objects.all()
    print(userpost)
    return render(request, 'blog/home.html', {"home":"text-green-500 border-b-4 border-green-500", 'posts':userpost})

def about_page(request):
    return render(request, 'blog/about.html', {"about":"text-green-500 border-b-4 border-green-500"})

def contact_page(request):
    if request.method == "POST":
        forms = ContactForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data["name"]
            email = forms.cleaned_data["email"]
            subject = forms.cleaned_data["subject"]
            contact = forms.cleaned_data["contact"]
            adress = forms.cleaned_data["adress"]
            usermsg = forms.cleaned_data["message"]
            subject = f"{subject}"
            message = f"Message: {usermsg} \n userName: {name}  \n useremail: {email} \n userPhoneNumber: {contact} \n useradress: {adress}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email,]
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, "Your message is sent sucessfully")
            forms = ContactForm()
    else:
        forms = ContactForm()
    return render(request, 'blog/contact.html', {"contact":"text-green-500 border-b-4 border-green-500", "forms": forms})

def signup_page(request):
    if request.method == "POST":
        forms = SignUpForm(request.POST)
        if forms.is_valid():
            user = forms.save()
            group = Group.objects.get(name="authors")
            user.groups.add(group)
            messages.success(request, "Account Created Sucessfully !!!")
            return HttpResponseRedirect("/login/")
            
            
    else:
        forms = SignUpForm()
    return render(request, 'blog/signup.html', {"forms": forms})

def login_page(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/dashboard/")
    else:
        if request.method == "POST":
            forms = LoginForm(request=request, data= request.POST)
            if forms.is_valid():
                uname = forms.cleaned_data["username"]
                upwd = forms.cleaned_data["password"]
                user = authenticate(username=uname , password = upwd)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect("/dashboard/")
        else:
            forms = LoginForm()
        return render(request, "blog/login.html", {"forms": forms})



def dashboard_page(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            forms = AuthorForm(request.POST)
            if forms.is_valid():
                utitle = forms.cleaned_data["title"]
                udesc = forms.cleaned_data["desc"]
                uauthor = forms.cleaned_data["author"]
                obj = Blogpost(title= utitle, desc = udesc, author= uauthor)
                obj.save()
                forms = AuthorForm()
        else:
            forms = AuthorForm()
        student_details = Blogpost.objects.all()
        return render(request, "blog/dashboard.html",{ "dashboard":"text-green-500 border-b-4 border-green-500","forms": forms, "student_details": student_details})
    else:
        return HttpResponseRedirect('/login/')

def delete_page(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            obj = Blogpost.objects.get(pk = id)
            obj.delete()
        return HttpResponseRedirect("/dashboard/")
    else:
        return HttpResponseRedirect("/login/")

def edit_page(request, id):
    if request.method == "POST":
        forms = AuthorForm(request.POST)
        if forms.is_valid():
            utitle = forms.cleaned_data["title"]
            udesc = forms.cleaned_data["desc"]
            uauthor = forms.cleaned_data["author"]
            user = Blogpost(id = id,title= utitle, desc = udesc , author = uauthor)
            user.save()
            return HttpResponseRedirect("/dashboard/")
        
    else:    
        user = Blogpost.objects.get(pk = id)
        forms = AuthorForm(instance= user)

    return render(request, "blog/edit.html", {"forms": forms})








    


def logout_page(request):
    logout(request)
    return HttpResponseRedirect("/login/")

