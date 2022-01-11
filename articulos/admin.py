from django.contrib import admin
from .models import Articulo

class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'valor',)

admin.site.register(Articulo, ArticuloAdmin)

