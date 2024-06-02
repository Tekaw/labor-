"""lx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from .views import delete_contract, index  # Import the index view function from your views.py file
from django.conf import settings  # Import settings
from django.conf.urls.static import static  # Import static function
from . import views 
from .views import delete_contract
from .views import contracts
from .views import signout


urlpatterns = [
    path('admin/', admin.site.urls),  # Mapping for the admin site
    path('', index, name='index'),    # Mapping for the root URL
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('contracts/', views.contracts, name='contracts'),
    path('add_contract/', views.add_contract, name='add_contract'),
    path('get_contracts/', views.get_contracts, name='get_contracts'),
    path('howitworks/', views.how_it_works, name='how_it_works'),
    path('contracts/<int:contract_id>/delete/', delete_contract, name='delete_contract'),
    path('contracts/', contracts, name='contracts'),
    path('signout/', signout, name='signout'),
    
]

# Serve static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

