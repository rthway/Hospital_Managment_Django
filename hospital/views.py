from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def About(request):
    return render(request,'about.html')

def Home(request):
    return render(request,'home.html')

def Contact(request):
    return render(request,'contact.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request, 'index.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')  # This line retrieves the value of the 'uname' field from the POST data submitted in the form.
        password = request.POST.get('pwd')  # This line retrieves the value of the 'pwd' field from the POST data submitted in the form.

        user = authenticate(request, username=username, password=password) # This line uses the authenticate function to check if the provided username and password match any user in the database. If a valid user is found, the user variable will contain the corresponding user object; otherwise, it will be None.
        if user is not None and user.is_staff: # This line checks whether the user variable is not None (i.e., a valid user object) and whether the user has the is_staff attribute set to True. The is_staff attribute is typically used to designate admin users in Django's default user model.
            login(request, user) # This line uses the login function to log in the user. It creates a user session and associates it with the current request.
            return redirect('home')  # Replace 'admin_home' with the URL name of your admin dashboard/homepage
        else:
            error_message = "Invalid credentials or insufficient permissions. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def admin_logout(request):
    logout(request)
    return redirect('admin_login')  # Redirect to the admin login page after logout
