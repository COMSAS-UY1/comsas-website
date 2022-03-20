from django.contrib import admin
from .models import (Project, Newsletter, Member, ContactRequest,
                     ContactAgency)

admin.site.register(ContactRequest)
admin.site.register(ContactAgency)
admin.site.register(Project)
admin.site.register(Newsletter)
admin.site.register(Member)
