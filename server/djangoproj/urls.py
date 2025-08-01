"""
Proyecto URLs (a nivel de proyecto)

Las `urlpatterns` listan las URL de nivel de proyecto.
Esto es donde enlazas las URLs de tus aplicaciones.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Ruta para el panel de administración de Django
    path('admin/', admin.site.urls),

    # Incluye las URLs de tu aplicación 'dealerships'
    # Esto le dice a Django que busque patrones de URL en el archivo urls.py de la aplicación
    path('', include('dealerships.urls')),
]
