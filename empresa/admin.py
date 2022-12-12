from django.contrib import admin
from .models import Empresa, Tecnologias


@admin.register(Tecnologias)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ['tecnologia',]


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 'email', 'cidade',
    ]
