from django.contrib import admin
from .models import Futbolista, Basquetbolista, Tenista, Avatar

# Register your models here.

admin.site.register(Futbolista)
admin.site.register(Basquetbolista)
admin.site.register(Tenista)
admin.site.register(Avatar)