from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm
from django.contrib import messages


#### SIGN UP VIEW ####
def create_account(request):
    """ Function responsible for creating accounts """
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.backend = 'users.backends.EmailBackend'
            user.save()
            login(request, user)
            print(f"EMAIL CREATE: {user.email}")
            if user.email == "admin@example.com":
                return redirect("view_admin_dashboard")
            return redirect("complaint-dashboard")

    else:
        form = SignUpForm()

    context = {"form": form}
    return render(request, "users/sign_up.html", context)


### LOGIN USER ###
def login_user(request):
    """ Handle user login """
    if request.user.is_authenticated:
        ## CHECK FOR OFFIFICAL
        print("EMAIL : ",request.user.email)
        if request.user.email == "admin@example.com":
            return redirect('view_admin_dashboard')
        else:
            return redirect('complaint-dashboard')

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Extract user
            user = authenticate(request, email=email, password=password, backend='users.backends.EmailBackend')

            if user is not None:
                login(request, user)

                ## OFFICIAL
                if email == "admin@example.com":
                    return redirect('view_admin_dashboard')
                else:
                    return redirect('complaint-dashboard')
            else:
                messages.error(request, "Invalid email or password. Please try again.")
        else:
            messages.error(request, "Please fill out the form correctly.")

    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, "users/login.html", context)


@login_required
def logout_user(request):
    """Handle user logout."""
    logout(request)  # This logs out the user
    return redirect('login-account')  # Redirect to the login page (or any other page)




def view_dashboard(request):
    """ Dashboard view for logged-in users """
    return render(request, "users/dashboard.html")

def view_main(request):
    """ Dashboard view for logged-in users """
    return render(request, "users/main.html")
