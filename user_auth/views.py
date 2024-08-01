from django.shortcuts import redirect, render
from django.views import generic
from django.urls import reverse_lazy
from user_auth.forms import RegForm
from .forms import CustomAuthenticationForm
from django.contrib.auth import login, authenticate

# Create your views here.

class UserRegisterView(generic.CreateView):
    """
    User registration view that uses Django's generic CreateView.
    
    Attributes:
        form_class (RegForm): Specifies the form to use for user registration. :noindex:
        template_name (str): The path to the template that will render the registration form. :noindex:
        success_url (str): The URL to redirect to upon successful registration. :noindex:
    """
    form_class = RegForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    # reverse_lazy is used to lazily reverse the 'login' URL name into a URL string.
    # This means that the actual URL is not computed until it is needed.

def user_login(request):
    """
    Handle user login requests.
    
    Handles both GET and POST requests. On GET requests, renders the login form.
    On POST requests, processes the form data to authenticate and log in the user.

    Args:
        request (HttpRequest): The request object containing the form data.
    
    Returns:
        HttpResponse: Renders the login form on GET requests or redirects to the home page 
                      on successful login. Renders the login form with errors on invalid 
                      login attempts.
    """
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'myband/login.html', {'form': form})
