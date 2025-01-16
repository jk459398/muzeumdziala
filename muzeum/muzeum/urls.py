from django.contrib import admin
from django.urls import path
from muzeum_app import views  # Upewnij się, że importujesz views z muzeum_app
from django.contrib.auth import views as auth_view
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('muzeum_app.urls')),
    path('login/', views.login_view, name='login'),  # Strona logowania
    path('start/', views.start_view, name='start')
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Strona startowa
  
]


