from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ArtistForm, ExhibitForm, LoanForm, StartForm
from .models import Artist, Exhibit, Loan, UserInfo
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import StartForm
from .models import UserInfo
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('start_form')  # Po zalogowaniu przekierowanie na start_form
        else:
            messages.error(request, 'Nieprawidłowy login lub hasło.')
    return render(request, 'muzeum_app/login.html')

def exhibit_list(request):
    exhibits = Exhibit.objects.all()
    return render(request, 'muzeum_app/exhibit_list.html', {'exhibits': exhibits})

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'muzeum_app/artist_list.html', {'artists': artists})


@login_required
def add_exhibit(request):
    form = ExhibitForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('add_exhibit')  # Po zapisaniu wraca do formularza
    return render(request, 'muzeum_app/add_exhibit.html', {'form': form})

@login_required  # Tylko zalogowani użytkownicy mogą dodawać artystów
def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_exhibit')  # Przekierowanie po zapisaniu artysty
    else:
        form = ArtistForm()
    return render(request, 'muzeum_app/add_artist.html', {'form': form})

@login_required  # Tylko zalogowani użytkownicy mogą dodawać eksponaty
@login_required
def add_exhibit(request):
    if request.method == 'POST':
        form = ExhibitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_exhibit')  # Możliwość dodawania kolejnych eksponatów
    else:
        form = ExhibitForm()
    return render(request, 'muzeum_app/add_exhibit.html', {'form': form})


@login_required  # Tylko zalogowani użytkownicy mogą dodawać wypożyczenia
def add_loan(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_loan')  # Możliwość dodawania kolejnych wypożyczeń
    else:
        form = LoanForm()
    return render(request, 'muzeum_app/add_loan.html', {'form': form})

@login_required  # Zabezpieczony widok dla start_view
def start_view(request):
    if request.method == 'POST':
        form = StartForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            user_email = form.cleaned_data['user_email']
            # Zapisz dane do bazy danych
            UserInfo.objects.create(user_name=user_name, user_email=user_email)
            # Przekaż także user_email do szablonu success.html
            return redirect('add_exhibit')  # Zamiast formularza, od razu przekieruj
    else:
        form = StartForm()

    return render(request, 'muzeum_app/add_exhibit.html', {'form': form})
    