from django.contrib import admin
from django.urls import path, include
from muzeum_app import views  
from django.contrib.auth import views as auth_view
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),  # Zamiast 'home', przypisujemy do 'start_view'
    path('login/', views.login_view, name='login'),
    path('zaloguj/', views.zalogujsie, name='zalogujsie'),  # Dodajemy alias do logowania
    path('start/', views.start_view, name='start_form'),
    path('guest/', views.guest_view, name='guest_view'),
    path('add_exhibit/', views.add_exhibit, name='add_exhibit'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Odkomentuj, jeśli potrzebne
]


