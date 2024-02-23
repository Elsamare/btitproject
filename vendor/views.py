# vendor/views.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import VendorForm
from .models import Vendor
from django.contrib.auth.forms import AuthenticationForm

# ... (Previous views)

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Log the user in
            login(request, form.get_user())
            return redirect('vendor_list')
    else:
        form = AuthenticationForm()

    return render(request, 'vendor/user_login.html', {'form': form})
def user_logout(request):
    logout(request)
    return redirect('vendor_list')

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('user_login')
    else:
        form = UserCreationForm()
    return render(request, 'vendor/user_signup.html', {'form': form})

def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendor/vendor_list.html', {'vendors': vendors})

def vendor_detail(request, pk):
    vendor = Vendor.objects.get(pk=pk)
    return render(request, 'vendor/vendor_detail.html', {'vendor': vendor})

def vendor_create(request):
    if request.method == 'POST':
        form = VendorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vendor_list')
    else:
        form = VendorForm()

    return render(request, 'vendor/vendor_form.html', {'form': form})

def vendor_update(request, pk):
    # Your implementation for vendor update
    pass

def vendor_delete(request, pk):
    # Your implementation for vendor update
    pass



