from django.shortcuts import redirect
from .models import UploadedFile

def user_has_uploaded_files(view_func):
    def _wrapped_view(request, *args, **kwargs):
        # Check if the user has uploaded books
        has_uploaded_books = UploadedFile.objects.filter(user=request.user).exists()
        
        if not has_uploaded_books:
            # Redirect to the upload_books page if no files exist
            return redirect('accounts:upload_books')
        
        # Proceed with the original view if files exist
        request.has_uploaded_books = has_uploaded_books
        return view_func(request, *args, **kwargs)
    
    return _wrapped_view
