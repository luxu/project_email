from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail


def send_mail_contract(request):
    recipient_list = ['zicadopv@terra.com.br']
    content = {'employee': 'João'}
    template = 'contract.html'
    message_html = render_to_string(template, content)
    template_txt = "contract.txt",
    message_txt = render_to_string(template_txt, content)
    subject = f'Contrato Digital'
    email_from = ''
    send_mail(
        subject,
        message_txt,
        email_from,
        recipient_list,
        fail_silently=False,
        html_message=message_html,
    )
    return HttpResponse("<h1> Email enviado com sucesso!! </h1>")


def email(request):
    context = {
        'logo': '',
        'id': '02',
        'tomador': 'Astolfo',
        'importancia_segurada': 'teste',
        'tipo_processo': 'teste'
    }
    recipient_list = ['zicadopv@terra.com.br']
    template = 'email.html'
    message_html = render_to_string(template, context)
    # template_txt = "txt/email.txt",
    template_txt = "contract.txt",
    message_txt = render_to_string(template_txt)
    subject = 'Testar o envio de e-mail'
    email_from = ''
    send_mail(
        subject,
        message_txt,
        email_from,
        recipient_list,
        fail_silently=False,
        html_message=message_html,
    )

    # return render(request, 'app/email.html', context)
    return HttpResponse("<h1> Email pela def: email enviado com sucesso!! </h1>")
