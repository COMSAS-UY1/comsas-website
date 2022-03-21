from django.shortcuts import redirect, render, HttpResponse
from django.core.mail.message import BadHeaderError
from django.views.generic import TemplateView
from .models import ContactRequest
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from django.utils.html import format_html
import re

class IndexView(TemplateView):
    template_name = "index.html"

    # add request for getting team member
    # add request for getting all projects
    # add request for getting all projects
    # add request for getting all partner
    # add request for getting contact information
    def contact(self, request):
        context = {
            'form': ContactForm
        }
        return render(request, self.template_name, context)
        
    def getContact(self, request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                message = form.cleaned_data['message']

            msg = "Si vous recevez ce mail c'est que votre message a bien été envoyé et est en cours de traitement. Voici les détails de votre message:..." + "\n\nNom Complet: " + name + "\nNuméro de téléphone : " + str(phone) + "\n\nMessage Envoyé : " + message + "\n\n\nMerci de nous avoir contacté. Nous espérons vous revoir très bientôt.\n\nTel : 656997810\nEmail : joefah2003@gmail.com\n\nEcrivez nous à propos de tout ce que vous voulez, a n'importe quel moment comme bon vous semble!"
            subjectEmail = "Contact Information from <" + f'{email}' + ">"

            # Test for phone field
            phonePattern = r"^(?=.{9}$)((6|2).*$)"
            if len(phone) < 9 and re.match(phonePattern, email):
                return HttpResponse('Invalid phone number provided...')

            # Send email (contact information) to required address
            try:
                send_mail(
                    subjectEmail, #subject
                    msg, #message
                    email, #from email
                    ['joelfah2003@gmail.com', email], #to email
                    )
            except BadHeaderError:
                return HttpResponse('Invalid header found')


            # Test if form data was saved and output corresponding flash message to confirm message placement or not.
            try:
                form.save()
                message_out_success = format_html(
                    f'Thanks for contacting us, <strong> {name} </strong> ! Your message has been sent successfully. You will be email a copy at <strong> {email} </strong> !'
                )
                messages.success(
                    request,
                    message_out_success
                )
            except:
                message_out_error = format_html(
                   f'Sorry, <strong> {name} </strong> ! There was a problem sending your message. Please reload and try again!'
                )
                messages.error(
                    request,
                    message_out_error
                )

                return redirect('index')
            else:
                form = ContactForm()
        return render(request, self.template_name, {'form': form})



class ContactView(TemplateView):
    template_name = "core/contact.html"


class NewsletterView(TemplateView):
    template_name = "core/newsletter.html"
