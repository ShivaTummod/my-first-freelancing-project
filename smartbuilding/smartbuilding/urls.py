"""
URL configuration for smartbuilding project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

# import views from the bot app
from bot import views as bot_views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=False), name='home'),
    path('admin/', admin.site.urls),
    path('signup/', bot_views.signup, name='signup'),
    path('login/', bot_views.login_view, name='login'),
    path('dashboard/', bot_views.dashboard, name='dashboard'),
    path('dashboard/<slug:page>/', bot_views.dashboard_page, name='dashboard_page'),
    path('dashboard/facilities/<slug:facility>/', bot_views.facility_detail, name='facility_detail'),
]

# Serve media files during development
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
