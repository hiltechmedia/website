from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django import forms
from .forms import ContactForm


def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract form data
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Process the form data, e.g., send an email
            send_mail(
                f'New Contact Form Submission from {full_name}',
                message,
                email,
                # Replace with your actual email
                ['hiltonorichards@gmail.com'],
                fail_silently=False,
            )
            print('Rendering contact_us.html')

            # Redirect to a success page
            return redirect('contact_success')  # Make sure you have this URL

    else:
        form = ContactForm()

    return render(request, 'contact_us.html', {'form': form})


def home(request):
    return render(request, 'home.html')


def music_studio(request):
    return render(request, 'music_studio.html')


def video_editing(request):
    return render(request, 'video_editing.html')


def contact_success(request):
    return render(request, 'contact_success.html')


def web_designing(request):
    return render(request, 'web_designing.html')
