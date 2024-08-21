from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.
def home_view(request):
    return render(request, 'pages/home.html')

def about_view(request):
    return render(request, 'pages/about.html')

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data["name"]
            email_from = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            
            send_mail(
                "Email from" + name,            # subject
                message,                        # content
                email_from,                     # from
                ["smokinjoenation@gmail.com"]   # to
            )
            
            return redirect('home')
        
        else:
            print("invalid form")
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})