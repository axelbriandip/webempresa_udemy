from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact (request):
    contact_form = ContactForm()

    # Si se hizo una petición 'post'.. Si se envío un mensaje por el formulario..
    if request.method == 'POST':
        # relleno la plantilla ContactForm con los campos del formulario
        contact_form = ContactForm(data = request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # suponemos que va todo bien..
            email = EmailMessage(
                'La ceffetiera: Nuevo mensaje de contacto', # asunto
                'De {} <{}>\n\nEscribió:\n\n{}'.format(name, email, content), # cuerpo
                'no-contestar@inbox.mailtrap.io',# email origen
                ['axelbriandip.rg@gmail.com'],# email destino
                reply_to=[email]# reply to
            )
            try:
                # si todo salió bien..
                email.send()
                return redirect(reverse('contact')+'?ok')
            except:
                # si algo salió mal..
                return redirect(reverse('contact')+'?fail')
            return redirect(reverse('contact')+'?ok') # reverse vendría a ser como el tag url

    return render(request, 'contact/contact.html', { 'form': contact_form })