from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContatoForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template import RequestContext

# Create your views here

def index(request):
    ''' Pagina inicial vitoria turismo '''
    return render(request, 'turismos/index.html')

def sobre(request):
    ''' Pagina sobre a empresa '''
    return render(request, 'turismos/sobre.html')

def contato(request):


    if request.method == 'POST':
        contato_form = ContatoForm(request.POST)
        if contato_form.is_valid():
            nome = contato_form.cleaned_data['nome']
            email = contato_form.cleaned_data['email']
            mensagem = contato_form.cleaned_data['mensagem']
            mensagem = 'Nome: {0} \E-mail: {1}\n{2}'.format(nome, email, mensagem)
            send_mail(
                'Contato Do Leverson teste', mensagem, settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL]
            )

            sucesso = True
            print('CONTATO_FORM  E VALIDO!!!!')

        else:
            print('CONTATO_FORM E INVALIDO!!!!')
            contato_form = ContatoForm()
        context = {'contato_form': contato_form}
        return render(request, 'turismos/contato.html', context)
    else:
        contato_form = ContatoForm()
        context = {'contato_form': contato_form}
        return render(request, 'turismos/contato.html', context)
