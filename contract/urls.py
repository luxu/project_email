from django.urls import path
from . import views


urlpatterns = [
    # path('', views.send_mail_contract, name="send-mail"),
    path('', views.email, name="enviar-mail"),
]
