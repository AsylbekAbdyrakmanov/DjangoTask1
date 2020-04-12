from django.urls import path
from .views import main_page, about, contacts, gallery

urlpatterns = [
    path('', main_page, name='index'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('gallery/', gallery, name='gallery'),

]