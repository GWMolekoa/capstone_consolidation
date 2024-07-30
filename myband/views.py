from django.shortcuts import get_object_or_404, render
from .models import Myband

def home(request):
    """
    Render the home page with specific bands.

    Retrieves bands 'The Beatles', 'Wu-Tang Clan', and 'The Temptations' from the database
    or raises a 404 error if any of them are not found. Passes these bands as context to 
    the 'home.html' template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered response for the 'home' page.
    """
    # Retrieve specific bands or raise 404 if not found
    beatles = get_object_or_404(Myband, name='The Beatles')
    wutang_clan = get_object_or_404(Myband, name='Wu-Tang Clan')
    temptations = get_object_or_404(Myband, name='The Temptations')

    # Context to pass to the template
    context = {
        'beatles': beatles,
        'wutang_clan': wutang_clan,
        'temptations': temptations
    }
    return render(request, 'myband/home.html', context)

def band_list(request):
    """
    Render a list of bands.

    Retrieves bands 'The Beatles', 'Wu-Tang Clan', and 'The Temptations' from the database
    or raises a 404 error if any of them are not found. Passes these bands as context to 
    the 'band_list.html' template.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered response for the 'band_list' page.
    """
    # Retrieve specific bands or raise 404 if not found
    beatles = get_object_or_404(Myband, name='The Beatles')
    wutang_clan = get_object_or_404(Myband, name='Wu-Tang Clan')
    temptations = get_object_or_404(Myband, name='The Temptations')

    # Context to pass to the template
    context = {
        'beatles': beatles,
        'wutang_clan': wutang_clan,
        'temptations': temptations
    }
    return render(request, 'myband/band_list.html', context)
