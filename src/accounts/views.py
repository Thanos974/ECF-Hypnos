from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
# from django.urls import reverse
# from .forms import ContactForm

User = get_user_model()

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        last_name = request.POST.get("last_name")
        first_name = request.POST.get("first_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, last_name=last_name, first_name=first_name, email=email, password=password)
        login(request, user)
        return redirect('book')
        
    return render(request, 'accounts/signup.html')


def login_user(request):
    if request.method == "POST":
        # Connecter l'utilisateur
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate( request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('book')

    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')



def contact_view(request):
#     form = ContactForm()
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.cleaned_data[]
#         return HttpResponseRedirect(reverse('remerciements'))

    return render(request, 'accounts/contact.html')

def remerciements_view(request):
    return HttpResponse("Merci de nous avoir contacté")


def dashboard(request):
    return render(request, 'accounts/dashboard.html')

