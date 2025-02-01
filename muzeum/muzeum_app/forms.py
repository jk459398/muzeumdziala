# muzeum_app/forms.py
from django import forms
from .models import *

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['first_name', 'last_name', 'birth_year', 'death_year']  

    def clean(self):
        cleaned_data = super().clean()
        birth_year = cleaned_data.get('birth_year')
        death_year = cleaned_data.get('death_year')

        if birth_year and death_year and birth_year >= death_year:
            raise forms.ValidationError("Rok urodzenia musi być mniejszy niż rok śmierci.")
        return cleaned_data


class ExhibitForm(forms.ModelForm):
    artist = forms.ModelChoiceField(
        queryset=Artist.objects.all(),
        required=False, 
        empty_label="Nieznany"  
    )

    class Meta:
        model = Eksponat
        fields = ['title', 'type', 'artist', 'status', 'cenny']

        
class SizeForm(forms.ModelForm):
    class Meta:
        model = Size
        fields = ['width', 'height', 'weight']

    def clean(self):
        cleaned_data = super().clean()
        width = cleaned_data.get('width')
        height = cleaned_data.get('height')
        weight = cleaned_data.get('weight')

        if width is not None and width < 0:
            self.add_error('width', 'Szerokość nie może być ujemna.')
        if height is not None and height < 0:
            self.add_error('height', 'Wysokość nie może być ujemna.')
        if weight is not None and weight < 0:
            self.add_error('weight', 'Waga nie może być ujemna.')

        return cleaned_data

class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ['name', 'city']
        
class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['name', 'description']


class ExhibitTransferForm(forms.Form):
    exhibit = forms.ModelChoiceField(queryset=Eksponat.objects.all(), label="Eksponat")
    gallery = forms.ModelChoiceField(queryset=Gallery.objects.all(), label="Miejsce")
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Data od")
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False, label="Data do")

class LoanForm(forms.Form):
    exhibit = forms.ModelChoiceField(queryset=Eksponat.objects.all(), label="Eksponat")
    institution = forms.ModelChoiceField(queryset=Institution.objects.all(), label="Miejsce")
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Data od")
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Data do")
