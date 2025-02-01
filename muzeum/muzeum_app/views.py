from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib import messages



def zalogujsie(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.POST.get('next')  
                return redirect('wybor')  
            else:
                messages.error(request, 'Niepoprawny login lub hasło.')
        else:
            messages.error(request, 'Błąd formularza logowania.')
    
    else:
        form = AuthenticationForm()

    return render(request, 'muzeum_app/zalogujsie.html', {'form': form})


def wybor(request):
    return render(request, 'muzeum_app/wybor.html')

@login_required  
def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wybor') 
    else:
        form = ArtistForm()
    return render(request, 'muzeum_app/add_artist.html', {'form': form})

def guest_view(request):
    eksponaty = Eksponat.objects.all()
    return render(request, 'muzeum_app/guest.html', {'exhibits': eksponaty})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('start_form')  
        else:
            messages.error(request, 'Nieprawidłowy login lub hasło.')
    return render(request, 'muzeum_app/login.html')

def exhibit_list(request):
    exhibits = Eksponat.objects.all()
    
    return render(request, 'muzeum_app/exhibit_list.html', {'exhibits': exhibits})

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'muzeum_app/artist_list.html', {'artists': artists})

def gallery_list(request):
    galleries = Gallery.objects.all()
    return render(request, 'muzeum_app/gallery_list.html', {'galleries': galleries})


def loan_history(request):
    loans = Loan.objects.all()
    return render(request, 'muzeum_app/loan_history.html', {'loans': loans})

def transfer_history(request):
    loans = Transfer.objects.all()
    return render(request, 'muzeum_app/transfer_history.html', {'transfers': loans})   

@login_required
def add_exhibit(request):
    if request.method == 'POST':
        exhibit_form = ExhibitForm(request.POST)
        size_form = SizeForm(request.POST)
        if exhibit_form.is_valid() and size_form.is_valid():
            new_size = size_form.save()
            new_exhibit = exhibit_form.save(commit=False)
            new_exhibit.size = new_size
            new_exhibit.save()
            return redirect('wybor')
    else:
        exhibit_form = ExhibitForm()
        size_form = SizeForm()
    return render(request, 'muzeum_app/add_exhibit.html', {'exhibit_form': exhibit_form, 'size_form': size_form})
        
@login_required  
def add_gallery(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wybor') 
    else:
        form = GalleryForm()

    return render(request, 'muzeum_app/add_gallery.html', {'form': form})


@login_required  
def add_institution(request):
    if request.method == 'POST':
        form = InstitutionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('wybor') 
    else:
        form = InstitutionForm()

    return render(request, 'muzeum_app/add_institution.html', {'form': form})

@login_required
def transfer_exhibit(request):
    if request.method == 'POST':
        form = ExhibitTransferForm(request.POST)
        if form.is_valid():
            exhibit = form.cleaned_data['exhibit']
            gallery = form.cleaned_data['gallery']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            if start_date > end_date:
                return render(request, 'muzeum_app/exhibit_transfer.html', {'form': form, 'error': 'Data rozpoczęcia nie może być późniejsza niż data zakończenia.'})
            
            transfer_item = Transfer(
                exhibit=exhibit,
                gallery=gallery,
                start_date=start_date,
                end_date=end_date
            )
            transfer_item.save()
            return redirect('wybor')
    else:
        form = ExhibitTransferForm()
    return render(request, 'muzeum_app/exhibit_transfer.html', {'form': form})

@login_required
def newloan(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            exhibit = form.cleaned_data['exhibit']
            institution = form.cleaned_data['institution']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            if start_date > end_date:
                return render(request, 'muzeum_app/loan_exhibit.html', {'form': form, 'error': 'Data rozpoczęcia nie może być późniejsza niż data zakończenia.'})
            
            if (end_date - start_date).days > 30:
                return render(request, 'muzeum_app/loan_exhibit.html', {'form': form, 'error': 'Różnica między datą rozpoczęcia a zakończenia nie może być większa niż 30 dni.'})
            
            transfer_item = Loan(
                exhibit=exhibit,
                place=institution,
                start_date=start_date,
                end_date=end_date
            )
            transfer_item.save()
            return redirect('wybor')
    else:
        form = LoanForm()
    return render(request, 'muzeum_app/loan_exhibit.html', {'form': form})
    

# @login_required  
# def loan_exhibit(request):
#     if request.method == 'POST':
#         form = LoanForm(request.POST)
#         if form.is_valid():
#             form.save()  
#             return redirect('loan_exhibit.html') 
#     else:
#         form = LoanForm()

#     return render(request, 'muzeum_app/loan_exhibit.html', {'form': form})

# @login_required
# def change_exhibit_status(request):
#     exhibit = Exhibit.objects.first()  
#     if request.method == 'POST':
#         form = ExhibitForm(request.POST, instance=exhibit)  
#         if form.is_valid():
#             form.save()  
#             return redirect('wybor')  
#     else:
#         form = ExhibitForm(instance=exhibit) 
#     return render(request, 'muzeum_app/change_exhibit_status.html', {
#         'form': form,
#         'exhibit': exhibit  
#     })

# @login_required
# def historia_wydarzen(request):
#     if request.method == 'POST':
#         form = LoanForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('wybor')  
#     else:
#         form = LoanForm()

#     wydarzenia_wypozyczen = LoanEvent.objects.all()  
#     return render(request, 'muzeum_app/history.html', {
#         'form': form, 
#         'wydarzenia_wypozyczen': wydarzenia_wypozyczen
#     })


