from django.contrib import admin
from .models import *

admin.site.register(Zona)
admin.site.register(TipoAula)
admin.site.register(Aula)

admin.site.register(Persona)
admin.site.register(Horario)
admin.site.register(HorarioPersona)


# Register your models here.
