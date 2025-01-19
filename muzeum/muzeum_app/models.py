from django.db import models
from datetime import timedelta
from django import forms

class UserInfo(models.Model):
    user_name = models.CharField(max_length=100)  # Pole user_name
    user_email = models.EmailField()  # Pole user_email
    user_password = models.CharField(max_length=255)

    def __str__(self):
        return self.user_name
    
class Artist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_year = models.IntegerField(null=True, blank=True)
    death_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Size(models.Model):
    height = models.FloatField()
    width = models.FloatField()
    weight = models.FloatField()

    def __str__(self):
        return f"Height: {self.height}, Width: {self.width}, Weight: {self.weight}"
    

class Exhibit(models.Model):
    title = models.CharField(max_length=200)
    exhibit_code = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=100)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, null=True, blank=True, on_delete=models.SET_NULL)
    is_in_museum = models.BooleanField(default=True)  # Czy eksponat jest w muzeum, czy wypożyczony
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.title

    def is_within_limit(self):
        """Sprawdza, czy wypożyczenie eksponatu nie przekroczyło 30 dni w danym roku."""
        year = self.start_date.year  # Weź rok rozpoczęcia wypożyczenia
        total_days = Loan.objects.filter(
            exhibit=self.exhibit,
            start_date__year=year  # Filtruj wypożyczenia w tym samym roku
        ).aggregate(
            total_days=models.Sum(models.F('end_date') - models.F('start_date'))
        )['total_days']

        # Sprawdź, czy całkowita liczba dni wypożyczenia w danym roku nie przekroczyła 30 dni
        return total_days <= timedelta(days=30)

    def __str__(self):
        return self.title
    
class Gallery(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name

class Loan(models.Model):
    exhibit = models.ForeignKey(Exhibit, on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=200)
    institution_city = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.exhibit.title} - {self.institution_name}"

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['exhibit', 'institution_name', 'institution_city', 'start_date', 'end_date']

    def clean(self):
        cleaned_data = super().clean()
        exhibit = cleaned_data.get('exhibit')
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        # Sprawdź, czy eksponat nie przekroczył limitu 30 dni wypożyczenia
        if exhibit and start_date and end_date:
            loan = Loan(exhibit=exhibit, start_date=start_date, end_date=end_date)
            if not loan.is_within_limit():
                raise forms.ValidationError("Eksponat przekroczył dozwolony limit 30 dni wypożyczenia w danym roku.")

        return cleaned_data