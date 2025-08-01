"""
Aplicación URLs (a nivel de aplicación 'dealerships')

Aquí defines las rutas específicas de tu aplicación.
"""
from django.urls import path
from . import views

# Define el nombre de la aplicación para evitar conflictos de nombres
app_name = 'dealerships'

urlpatterns = [
    # Ruta para la página de inicio que muestra la lista de concesionarios
    path('', views.get_dealerships, name='index'),

    # Ruta para la página 'acerca de'
    path('about/', views.about, name='about'),

    # Ruta para la página de 'contacto'
    path('contact/', views.contact, name='contact'),

    # Ruta para ver los detalles de un concesionario y sus reseñas
    # El <int:dealer_id> es un parámetro dinámico que captura el ID del concesionario
    path('<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),

    # Ruta para el formulario de publicación de una nueva reseña
    path('postreview/<int:dealer_id>/', views.post_review, name='post_review'),
]
