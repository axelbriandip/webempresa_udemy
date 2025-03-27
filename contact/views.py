from django.shortcuts import render, redirect
from django.urls import reverse # 'reverse' sería el equivalente al tag url
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # si todo va bien, enviamos el email
            email = EmailMessage(
                'La caffetiera 2025: Nuevo mensaje', # asunto
                'De {} <{}>\n\nEscribió:\n\n{}'.format(name, email, content), # cuerpo
                'no-contestar@inbox.mailtrap.io', # email origen
                # ['sandbox.smtp.mailtrap.io'], # email destino
                ['clubolimpo.rg@gmail.com'], # email destino
                reply_to=[email]
            )

            try:
                email.send()
                # todo fue bien, redireccionamos a OK
                return redirect(reverse('contact')+'?ok')
            except Exception as e:
                # algo salió mal, redireccionamos a FAIL
                print(f"Error al enviar el correo: {e}")
                return redirect(reverse('contact')+'?fail')


    return render(request, 'contact/contact.html', { 'form': contact_form })