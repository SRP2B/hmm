from django.contrib import admin
from .models import Nauczyciel, Sprawdzian, Przedmiot
# Register your models here.

admin.site.register(Nauczyciel)
admin.site.register(Sprawdzian)
admin.site.register(Przedmiot)