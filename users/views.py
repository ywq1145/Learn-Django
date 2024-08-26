from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm


def logout_view(request):
    """Log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse('index'))



def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = CustomUserCreationForm()
    else:
        # Process completed form.
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            newuser = form.save()
            authenticated_user = authenticate(username=newuser.username,
                                              password=request.POST['password1'])
            if authenticated_user is not None:
                login(request, authenticated_user)
                return HttpResponseRedirect(reverse('index'))
    context = {'form': form}
    return render(request, 'register.html', context)
