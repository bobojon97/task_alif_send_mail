from django.urls import path
from mail_send.views import mail, contact

urlpatterns = [
    path('', mail, name='home'),
    path('contact/', contact, name='contact'),
]