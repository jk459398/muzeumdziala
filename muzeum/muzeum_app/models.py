from django.db import models
from datetime import timedelta
from django import forms

class UserInfo(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
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
    is_in_museum = models.BooleanField(default=True)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    def is_within_limit(self):
        year = self.start_date.year
        total_days = Loan.objects.filter(
            exhibit=self,
            start_date__year=year
        ).aggregate(
            total_days=models.Sum(models.F('end_date') - models.F('start_date'))
        )['total_days'] or timedelta(days=0)

        return total_days <= timedelta(days=30)

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

        if exhibit and start_date and end_date:
            if not exhibit.is_within_limit():
                raise forms.ValidationError("Eksponat przekroczył dozwolony limit 30 dni wypożyczenia w danym roku.")

        return cleaned_data