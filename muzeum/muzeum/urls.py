from django.contrib import admin
from django.urls import path, include
from muzeum_app import views

urlpatterns = [
    path('zaloguj/', views.zalogujsie, name='zalogujsie'),
    path('wybor/', views.wybor, name='wybor'),
    path('add_artist/', views.add_artist, name='add_artist'),
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('guest/', views.guest_view, name='guest_view'),
    path('exhibit_list/', views.exhibit_list, name='exhibit_list'),
    path('artist_list/', views.artist_list, name='artist_list'),
    path('gallery_list/', views.gallery_list, name='gallery_list'),
    path('add_exhibit/', views.add_exhibit, name='add_exhibit'),
    path('add_gallery/', views.add_gallery, name='add_gallery'),
    path('add_institution/', views.add_institution, name='add_institution'),
    path('exhibit_transfer/', views.transfer_exhibit, name='exhibit_transfer'),
    path('loan_exhibit/', views.newloan, name='loan_exhibit'),
    path('loan_history/', views.loan_history, name='loan_history'),
    path('transfer_history/', views.transfer_history, name='transfer_history'),
    # path('history/', views.historia_wydarzen, name='history'),
    # path('exhibit_change_status/', views.change_exhibit_status, name='change_exhibit_status'),
]


