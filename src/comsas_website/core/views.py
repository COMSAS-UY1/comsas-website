from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "core/index.html"

    # add request for getting team member
    # add request for getting all projects
    # add request for getting all projects
    # add request for getting all partner
    # add request for getting contact information



class ContactView(TemplateView):
    template_name = "core/contact.html"


class NewsletterView(TemplateView):
    template_name = "core/newsletter.html"
