# relationship_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from .models import Book 
from .models import Library 

# Function-Based View: List all books
def list_books(request):
    books = Book.objects.all()  
    return render(request, 'relationship_app/list_books.html', {'books': books})  

# Class-Based View: Display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  
    context_object_name = 'library' 

#Authentication Views
def home_view(request):
    return render(request, 'relationship_app/home.html')

#User registration
def register_views(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # log in user immediatly
            return redirect('home') # REdirect after registartion
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html',{'form':form})

# User logiin
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') # Redirect after login
        else:
            form = AuthenticationForm()
        return render(request, 'relationship/login.html',{'form' : form})
    
# User logout
@login_required
def logout_view(request):
    logout(request)
    return render(request, ' relationship/logout.html')