"""
Aplicación Views (a nivel de aplicación 'dealerships')

Aquí se encuentra la lógica para manejar las solicitudes web
y renderizar las plantillas HTML correspondientes.
"""
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Importa el cliente API (asumiendo que tienes un archivo api_client.py)
# from .api_client import get_dealerships, get_reviews_for_dealer, add_review

def get_dealerships(request):
    """
    Vista para mostrar la página de inicio con la lista de concesionarios.
    """
    # Lógica para obtener datos de concesionarios desde la API
    # dealerships = get_dealerships()
    # return render(request, 'dealerships/index.html', {'dealerships': dealerships})

    # Ejemplo de datos estáticos para propósitos de demostración
    dealerships = [
        {'id': 1, 'name': 'Concesionario Norte', 'city': 'Ciudad de México'},
        {'id': 2, 'name': 'Concesionario Sur', 'city': 'Guadalajara'},
    ]
    return render(request, 'dealerships/index.html', {'dealerships': dealerships})

def about(request):
    """
    Vista para mostrar la página 'Acerca de'.
    """
    return render(request, 'dealerships/about.html')

def contact(request):
    """
    Vista para mostrar la página de 'Contacto'.
    """
    return render(request, 'dealerships/contact.html')

def get_dealer_details(request, dealer_id):
    """
    Vista para mostrar los detalles de un concesionario y sus reseñas.
    """
    # Lógica para obtener los detalles del concesionario y sus reseñas desde la API
    # dealer = get_dealer_by_id(dealer_id)
    # reviews = get_reviews_for_dealer(dealer_id)
    # return render(request, 'dealerships/dealer_details.html', {'dealer': dealer, 'reviews': reviews})

    # Ejemplo de datos estáticos para propósitos de demostración
    dealer = {'id': dealer_id, 'name': 'Concesionario {}'.format(dealer_id)}
    reviews = [
        {'text': 'Excelente servicio.', 'sentiment': 'positive'},
        {'text': 'Experiencia regular.', 'sentiment': 'negative'},
    ]
    return render(request, 'dealerships/dealer_details.html', {'dealer': dealer, 'reviews': reviews})

def post_review(request, dealer_id):
    """
    Vista para manejar el envío del formulario de una nueva reseña.
    """
    if request.method == 'POST':
        # Lógica para procesar la reseña y enviarla a la API
        # review_text = request.POST.get('review_text')
        # ...
        # add_review(dealer_id, review_text)
        return redirect('dealerships:dealer_details', dealer_id=dealer_id)

    # Si la solicitud no es POST, simplemente muestra el formulario
    return render(request, 'dealerships/post_review.html', {'dealer_id': dealer_id})
