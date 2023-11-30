from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
import logging

# ... (your other imports)

def home_view(request):
    login_form = AuthenticationForm()
    registration_form = UserCreationForm()

    if request.method == 'POST':
        if 'submit_login' in request.POST:
            login_form = AuthenticationForm(request, request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('landing')
                else:
                    login_form.add_error(None, 'Invalid username or password.')

        elif 'submit_register' in request.POST:
            registration_form = UserCreationForm(request.POST)
            if registration_form.is_valid():
                registration_form.save()
                username = registration_form.cleaned_data.get('username')
                password = registration_form.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('landing')

    context = {
        'login_form': login_form,
        'registration_form': registration_form
    }
    return render(request, 'myapp/home.html', context)


def landing_view(request):
    if not request.user.is_authenticated:
        return redirect('home')
    return render(request, 'myapp/landing.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def service_request_view(request):
    if request.method == 'POST':
        service_type = request.POST.get('service_type')
        description = request.POST.get('description')
        contact_email = request.POST.get('contact_email')

        # Construct the email content
        subject = f'New Service Request: {service_type}'
        message = f'Service Type: {service_type}\nDescription: {description}\nContact Email: {contact_email}'

        # Specify the recipient email (you can store this in settings or models)
        recipient_email = 'bagner@awlokitf.com'  # Replace with your desired recipient email

        try:
            # Send the email using SendGrid
            send_mail(
                subject,
                message,
                'bagner@awlokitf.com',
                [recipient_email],

            )

            # Process the form data (you can add your logic here)

            # Redirect with a success message
            print('poop')
            messages.success(request, 'Your service request has been submitted successfully.')
            return redirect(reverse('landing'))

        except Exception as e:
            # Log the error for debugging
            logging.error(f"Error sending email: {e}")

            # Handle any exceptions that may occur during email sending
            messages.error(request, f'An error occurred while processing your request. Please try again later.')

    # Render the form page if not a POST request
    return render(request, 'myapp/landing.html')
