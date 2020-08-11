from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.

def contact(request):
    form = ContactForm()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid:
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            email = EmailMessage(
                "La Caffettiera: Neevo mensaje", #subject
                "De {} <{}>\n\nEscribio:\n\n{}".format(name,email.content), #body
                "no_replay@inbox.mailtrap.io", #origin email
                [''], #email to
                replay_to[email], #replay to
            )
            try:
                email.send()
                return redirect(reverse('contact')+'?ok')
            except:
                return redirect(reverse('contact')+'?err')
                
    return render(request, 'contact/contact.html', context)
