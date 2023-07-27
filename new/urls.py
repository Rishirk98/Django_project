"""
URL configuration for new project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from newapp import views
from newapp.views import tittle, edit_title, show_title, delete_title, superadd
from django.conf import settings# for image library
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tittle/',superadd),# function to add photo
    path('edit/<int:u_id>', edit_title, name='edit_title'), #for update the user
    path('show/', show_title, name="show_title"),
    path('delete/<int:u_id>', delete_title, name='delete_title') #for delete the user

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #image load shortcut in django library
