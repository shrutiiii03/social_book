from django.shortcuts import render, redirect
from .forms import RegisterForm, UploadBookForm
from .models import CustomUser, UploadedFile
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from rest_framework.authtoken.models import Token
from django.contrib.auth import login

from rest_framework import generics, permissions
from .serializers import UploadedFileSerializer

from .decorators import user_has_uploaded_files

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view

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

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class CustomLoginView(LoginView):
        template_name = 'accounts/login.html'

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def authors_and_sellers(request):
    users = CustomUser.objects.filter(public_visibility=True).exclude(is_superuser=True)
    return render(request, 'accounts/authors_and_sellers.html', {'users': users})

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
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

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@user_has_uploaded_files
def my_books_dashboard(request):
    # Retrieve all uploaded books for the current user
    books = UploadedFile.objects.filter(user=request.user)
    return render(request, 'accounts/my_books.html', {'books': books})

class UserUploadedFilesView(generics.ListAPIView):
    serializer_class = UploadedFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UploadedFile.objects.filter(user=self.request.user)


