from django.contrib import admin
from django.urls import path, include
from muzeum_app import views  # Upewnij się, że importujesz views z muzeum_app
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('muzeum_app.urls')),  # Włącz wszystkie ścieżki z aplikacji
    path('login/', views.login_view, name='login'),  # Strona logowania
    path('start/', views.start_view, name='start'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Wylogowanie
]










