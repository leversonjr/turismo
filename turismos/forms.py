from django import forms

class ContatoForm(forms.Form):

    nome = forms.CharField(label='Nome', required=True)
    email = forms.EmailField(label='Email')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea(), required=True)

    def __init__(self, *args, **kwargs):
        super(ContatoForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['nome'].widget.attrs['placeholder'] = 'Digite seu nome'
        self.fields['email'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['email'].widget.attrs['placeholder'] = 'Digite seu email'
        self.fields['mensagem'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['mensagem'].widget.attrs['placeholder'] = 'Escreva sua mensagem...'