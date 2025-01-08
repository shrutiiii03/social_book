
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import UserUploadedFilesView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # View to get access and refresh tokens
    TokenRefreshView,     # View to refresh the access token
)

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('accounts/', include('accounts.urls')), 
    path('', lambda request: redirect('accounts:login')),  
    # Token generation
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Token refresh
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
