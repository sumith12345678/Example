from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .models import *

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if password1 != password2:
                messages.info(request, 'Passwords does not match')
            else:
                User.objects.create_user(
                    username=username,
                    password=password1,
                )
                messages.success(request, 'Account was created for '+ username)
                return redirect('login')
        return render(request, 'registration.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = auth.authenticate(request, username = username, password = password, )

            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect!!!')

    
            return redirect('home')  
        return render(request,'login.html')



@login_required(login_url='login')
def home(request):
    if request.user.is_staff == False:
        book=Book.objects.filter(status=True).all()
        if request.method == 'POST':
            cat = request.POST.get('category')
            search = request.POST.get('search')
            if search:
                book=book.filter(Book_name__icontains=search)
            if cat :
                book=book.filter(category=cat)
            
        return render(request,"home.html",context={'book':book})
    else:
        book=Book.objects.all()
        
        return render(request,"admin.html",context={'book':book})

def logoutPage(request):
    auth.logout(request)
    return redirect('login')


def change(request, id):
    book = Book.objects.get(id=id)
    if book.status == True:
        book.status = False
        book.save()
    else:
        book.status = True
        book.save()        
    return redirect('home')

def add(request):
    if request.method =='POST':
        book=request.POST.get('book_name')
        category=request.POST.get('category')
        image=request.FILES.get('image')
        author=request.POST.get('author')
        price=request.POST.get('price')
        status=request.POST.get('status')
      
        Book.objects.create(
            Book_name=book,
            category=category,
            image=image,
            Author=author,
            price=price,       
            status=status,
        )
        return redirect('home')
    return render(request,'add.html')
    

# 