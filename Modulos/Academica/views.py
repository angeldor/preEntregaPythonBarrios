from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def contactForm(request):
    return render(request, "contactForm.html")

def contact(request):
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + " / Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIl_HOST_USER
        email_para = ["ab0180333@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request,"contactoExitoso.html")
    return render(request, "contactForm.html")
        