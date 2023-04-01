from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage
# Create your views here.
#vista contact
def contact(request):
    contactForm = ContactForm()
    #instancia del formulario
    #print("Tipo de petición: {}".format(request.method))
    if request.method == "POST":
        contactForm = ContactForm(request.POST)
        if contactForm.is_valid():
            name=request.POST.get('name',' ')
            email=request.POST.get('email',' ')
            message=request.POST.get('message',' ')
            #enviar correo
            email=EmailMessage(
                "World: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name,email,message),
                "correoprueba@inbox.mailtrap.io",
                ["aleister200213@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                #algo no ha ido bie    
                return redirect(reverse('contact')+"?fail")
    return render(request, "contact/contact.html", {'contactForm':contactForm})