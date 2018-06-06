from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here

def index(request):
    ''' Pagina inicial vitoria turismo '''
    return render(request, 'turismos/index.html')

def contato(request):
    sucesso: False
    if request.method == 'POST':
        contato_form = ContatoForm(request.POST)
        if contato_form.is_valid():
            nome = contato_form.cleaned_data['nome']
            email = contato_form.cleaned_data['email']
            mensagem = contato_form.cleaned_data['mensagem']
            mensagem = 'None: {0} \E-mail: {1}\n{2}'.format(nome, email, mensagem)
            send_mail(
                'Contato Do Leverson teste', mensagem, settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL]
            )
            sucesso = True

        else:
            contato_form = ContatoForm()
            context = {
                'contato_form': contato_form,
                'sucesso': sucesso
            }
            return render(request, 'turismos/contato.html', context)