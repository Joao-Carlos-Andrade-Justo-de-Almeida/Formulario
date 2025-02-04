from django.contrib import admin
from .models import FormularioModel
# Register your models here.

@admin.register(FormularioModel)

class FormularioModelAdmin(admin.ModelAdmin):
    list_display = ['data', 'turno', 'conferente', 'cliente', 'transportadora', 'num_nota', 'quantidade_cx', 'quantidade_recebidas', 'motivo', 'setor','valor']
    search_fields = ['data', 'conferente', 'cliente', 'num_nota', 'motivo', 'setor']
