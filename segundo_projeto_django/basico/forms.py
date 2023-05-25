'''
Comando para a verificação do formulárai - neste caso - forms.is_valid()
Comando para criação da html
Comando no terminal do python com o abiente do django - python manage.py shell

'''

from django import forms

class ContatosForms(forms.Form):

    nome = forms.CharField(label='Nome')
    endereço= forms.CharField(label='endereço')
    email = forms.EmailField(label= 'Email')
    mensagem = forms.CharField( label='Mensagem', widget=forms.Textarea)
    data = forms.DateField(label='Data', required=False)# O required marca o campo como não obrigatório.

   