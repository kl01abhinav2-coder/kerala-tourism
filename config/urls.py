from django.contrib import admin
from django.urls import path, include
from tourism import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Fixed the .path to .urls
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('signup/', views.signup, name='signup'),
    path('book/<int:dest_id>/', views.book, name='book_now'),
]

# This allows the Munnar images to show up
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)