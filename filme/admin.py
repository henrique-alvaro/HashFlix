from django.contrib import admin
from .models import Filme, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin


class ListadeFilmes(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'categoria', 'publicado',)
    list_display_links = ('id', 'titulo',)
    search_fields = ('titulo',)
    list_filter = ('categoria',)
    list_editable = ('publicado',)
    list_per_page = 10


# Só existe porque a gente quer que no admin apareça o campo personalizado filmes_vistos
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {'fields': ('filmes_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Filme, ListadeFilmes)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)


