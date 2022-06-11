from django.contrib import admin
from .models import Livro, Emprestimo, Usuario
from django.contrib.auth.admin import UserAdmin

campos = list(UserAdmin.fieldsets)
campos.append(
    ("Adicionais", {'fields': ('ra', 'ano', 'turma',)})
)

UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Livro)
admin.site.register(Emprestimo)
admin.site.register(Usuario, UserAdmin)
