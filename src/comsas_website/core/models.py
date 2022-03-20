from django.db import models
from django_tuieditor.models import MarkdownField

class ContactRequest(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.name} -- {self.email}"


class Project(models.Model):

    name = models.CharField(max_length=200)
    description = MarkdownField()
    image = models.ImageField(upload_to='project',
                              default='project/no_picture.png')
    lien = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f" {self.name}  -- {self.description}"


class ContactAgency(models.Model):

    phone_number = models.CharField(max_length=200)
    localisation = models.CharField(max_length=200, null=True, blank=True)

    email = models.EmailField()
    whatsapp = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)
    telegram = models.URLField(max_length=200)
    facebook = models.URLField(max_length=200)
    linkedlin = models.URLField(max_length=200)

    github = models.URLField(max_length=200)


class Member(models.Model):

    name = models.CharField(max_length=200)
    poste = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='team', default='team/no_picture.png')
    description = MarkdownField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    linkedlin = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f" {self.nom} -- {self.poste}"


class Partner(models.Model):

    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='Client',
                             default='Client/no_picture.png')
    web_site = models.URLField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    description = MarkdownField(max_length=200, null=True, blank=True)
    


class Newsletter(models.Model):

    email = models.EmailField(null=True)

    def __str__(self):
        return f" {self.email}"
