from django.urls import path
from . import views

app_name = 'website'
urlpatterns = [
    path('', views.home, name='home'),
    path('servicios/', views.services, name='services'),
    path('nosotros/', views.about, name='about'),
    path('reserva/', views.booking, name='booking'),
    path('contacto/', views.contact, name='contact'),

    # Blog list & detail
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
]