from django.urls import path
from accounts import views
from .views import CustomLoginView, authors_and_sellers, UserUploadedFilesView

app_name = 'accounts' 
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),  
    path('authors-and-sellers/', authors_and_sellers, name='authors_and_sellers'), 
    path('upload-books/', views.upload_books, name='upload_books'), 
    path('my_books/', views.my_books_dashboard, name='my_books'), 
    path('user-files/', UserUploadedFilesView.as_view(), name='user-files'),
]
