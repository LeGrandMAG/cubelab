from email import message
from time import sleep
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from accounts.models import Product, Profile, EarlyUser
from .forms import EarlyUserForm, UserForm 
from django.contrib import messages

from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate, login, logout



# Home view

def UserDisplay(request, pk):
    user = Profile.objects.get(id=pk)

    context = {'user': user}
    return render(request, 'base.html', context)
def Home(request):

    if request.method == 'POST':
        if (request.POST.get('nom')!='' and request.POST
        early_user = EarlyUser.objects.create(
            nom = request.POST.get('nom'), 
            phone = request.POST.get('phone'))
        """
        nom = request.POST['nom']
        phone = request.POST['phone']
        early_user = EarlyUser.objects.create(nom=nom, phone=phone)"""
            
        sleep(2)
        return redirect('Home')

    
    
    return render(request, 'accounts/index.html')


#About us view
def About(request):
    return render(request, 'accounts/about.html')


#Thank you for registering your product
def thankyou(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'accounts/thankyou.html', context )


#LoginPage
def LoginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('Home')
    error1 = False
    error2 = False
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = Profile.objects.get(email=email)
        except:
            error1 = True
            #messages.error(request, '')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            error2 = True
    
    context = {'page': page}
    return render(request, 'accounts/login.html', context)



# Form for registering a product
def ProductRegistration(request):
    meme = 0
    if request.method == 'POST':
        form = UserForm(request.POST)
        model = request.POST.get('model')
        
        if form.is_valid():
            nom = request.POST['nom']
            imei = request.POST['imei']
            price = request.POST['price']
            battery = request.POST['battery']
            model = request.POST['model']
            cat = request.POST['cat']
            fissure1 = request.POST['fissure1']
            fissure2 = request.POST['fissure2']
            image = request.POST['image']
            memory = request.POST['memory']
            product = Product.objects.create(nom=nom,model=model, imei=imei, price=price, cat=cat, battery=battery, image=image, fissure1=fissure1, fissure2=fissure2, memory=memory)
            
            return render(request, 'accounts/index.html')
        else:
            meme =1
            
    else:
        form = UserForm()
        meme = 0
        
    return render(request, 'accounts/form.html', {'form': form, 'meme': meme })

