# muzeum_app/forms.py
from django import forms
from .models import Artist, Exhibit, Size, Gallery, Loan, UserInfo  # Dodaj UserInfo, jeśli jest to wymagane

# Formularz dla Artysty
class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['first_name', 'last_name', 'birth_year', 'death_year']

# Formularz dla Eksponatu
class ExhibitForm(forms.ModelForm):
    class Meta:
        model = Exhibit
        fields = ['title', 'exhibit_code', 'type', 'size', 'artist']

# Formularz dla Wypożyczenia
class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['exhibit', 'institution_name', 'institution_city', 'start_date', 'end_date']

# Formularz Startowy
class StartForm(forms.ModelForm):
    class Meta:
        model = UserInfo  # Upewnij się, że masz model UserInfo w models.py
        fields = ['user_name', 'user_email', 'user_password']  # Przykład pól formularza


