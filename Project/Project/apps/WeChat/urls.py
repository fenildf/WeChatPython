from django.urls import path
from . import message

urlpatterns = [
    path(r'message/', message.reply),
    path(r'token/', message.token),
]