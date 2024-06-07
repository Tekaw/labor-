from django.urls import path
from .views import home_view, landing_view, logout_view, service_request_view

urlpatterns = [
    path('', home_view, name='home'),
    path('landing/', landing_view, name='landing'),
    path('logout/', logout_view, name='logout'),
    path('service-request/', service_request_view, name='service_request'),


]
