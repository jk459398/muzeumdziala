from django.contrib import admin
from django.urls import path, include
from muzeum_app import views  # Upewnij się, że importujesz poprawnie widoki
from django.contrib.auth import views as auth_view
from django.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('', views.start_view, name='start_form'),  # Zamiast 'home', przypisujemy do 'start_view'
    path('login/', views.login_view, name='login'),
    path('start/', views.start_view, name='start_form'),
    path('add_exhibit/', views.add_exhibit, name='add_exhibit'),
    path('add_artist/', views.add_artist, name='add_artist'),
    path('add_loan/', views.add_loan, name='add_loan'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Odkomentuj, jeśli potrzebne
]


