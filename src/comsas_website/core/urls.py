from django.urls import path
from core.views import IndexView, ContactView, NewsletterView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),    
    path('contact-us/', ContactView.as_view(), name='contact-us'),
    path('subcribe', NewsletterView.as_view(), name='subcribe')
]
