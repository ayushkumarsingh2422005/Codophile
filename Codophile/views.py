from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from MoreModels.models import UserDetail

def codophile_homepage(request):
    dect = {"a": 'ayush kumar singh'}
    return render(request, 'homepage.html', dect)
def profile(request, slug):
    if UserDetail.objects.filter(user_name=slug).exists():
        user_prof = UserDetail.objects.get(user_name=slug)
        user_detail = User.objects.get(username=slug)
        prams = {
            "user_prof": user_prof,
            "user_detail": user_detail
        }
        return render(request, 'profile.html', prams)
    else:
        prams = {
            "user_prof": "Not_Found",
            "user_name": slug
        }
        return render(request, 'profile.html', prams)
def direcrprofie(request):
    return redirect("/")
def codophile_about(request):
    return render(request, 'aboutus.html')

def handle_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if username == "Not_Found":
            messages.warning(request, "User Name Cant be Not_Found as it is reserved")
            return redirect('/signup')
        if not username.isalnum():
            messages.warning(request, username+" is not a valid name, Letters, digits and @/./+/-/_ only.")
            return redirect('/signup')
        if password1!=password2:
            messages.warning(request, "pass in both field dont match with each other")
            return redirect('/signup')
        if len(password1) < 6:
            messages.warning(request, "password cant be smaller then 6 len")
            return redirect('/signup')
        if User.objects.filter(username = username).exists():
            messages.warning(request, "username allready exis")
            return redirect('/signup')
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request, "Account created sucessfully")
        # login
        user = authenticate(username=username, password=password1)
        if user is not None:
            login(request, user)
            # creating database
            userdetail = UserDetail(user_name=username)
            userdetail.save()
            return redirect('/')
        return redirect('/signup')
    else:
        return render(request, 'signup.html')

def handle_signin(request):
    if request.method == "POST":
        username = request.POST['username']
        login_pass = request.POST['login_pass']
        user = authenticate(username=username, password=login_pass)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Either user name or password didnt matched correctlly ")
            return redirect('/login')
    else:
        return render(request, 'login.html')

def handle_logout(request):
    logout(request)
    return redirect('/')

# custom 404 view
def custom_404(request, exception):
    return render(request, '404.html', status=404)