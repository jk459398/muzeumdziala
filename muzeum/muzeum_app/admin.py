from django.contrib import admin
from .models import Artist, Exhibit, Size, Gallery, Loan

admin.site.register(Artist)
admin.site.register(Exhibit)
admin.site.register(Size)
admin.site.register(Gallery)
admin.site.register(Loan)
