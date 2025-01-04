from django.shortcuts import render, redirect
from .forms import RegisterForm, UploadBookForm
from accounts.models import CustomUser
from django.contrib.auth.views import LoginView
from .models import UploadedFile
from django.contrib.auth.decorators import login_required

def register(request):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.save()
                return redirect('login')
        else:
            form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})

class CustomLoginView(LoginView):
        template_name = 'accounts/login.html'

def authors_and_sellers(request):
    users = CustomUser.objects.filter(public_visibility=True).exclude(is_superuser=True)
    return render(request, 'accounts/authors_and_sellers.html', {'users': users})

@login_required
def upload_books(request):
    if request.method == 'POST':
        form = UploadBookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user  
            book.save()
            return redirect('accounts:upload_books')  
    else:
        form = UploadBookForm()


    books = UploadedFile.objects.filter(user=request.user)
    return render(request, 'accounts/upload_books.html', {'form': form, 'books': books})