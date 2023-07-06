from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
 #Create your views here.

def user_login(request):
    context = dict()
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request , messages.SUCCESS , "Giriş işlemi Başarılı")
            nextUrl = request.GET.get("next", None)      # login olurken next sayfasina gitmesini saglar.
            if nextUrl is None:                                
                return redirect("index")
            else:
                return redirect(nextUrl)
        else:
            messages.add_message(request , messages.ERROR , "Kullanıcı Adı veya Parola yanlış")
            return render(request,"account/login.html")
    else:
        return render (request, "account/login.html", context)


def user_register(request):
    context = dict()
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password != repassword :
            messages.add_message(request , messages.ERROR , "Parola eşleşmiyor.")
            return render(request,'account/register.html' )

        if User.objects.filter(username = username).exists():
            messages.add_message(request , messages.ERROR , "Kullanıcı Adı kullanılıyor.")
            return render(request,'account/register.html')
            
        if User.objects.filter(email = email).exists():
            messages.add_message(request , messages.ERROR , "Email kullanılıyor.")
            return render(request,'account/register.html',)
                
        user = User.objects.create_user(username = username , email =email, password = password)
        user.save()
        messages.add_message(request , messages.SUCCESS , "Kayıt işlemi Başarılı.")
        return redirect('account:user_login')
    else:
        return render (request, "account/register.html", context)


def user_logout(request):
    logout(request)
    messages.add_message(request , messages.ERROR , "Cıkış işlemi Başarılı.")
    return redirect("index")

