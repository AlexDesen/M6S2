from django import forms

class ReservaForms(forms.Form):
    nome_do_pet = forms.CharField(label='Nome do pet')
    telefone = forms.CharField(label='Telefone')
    data_da_reserva = forms.DateField(label='Data de reserva')
    observacao = forms.CharField(label='Observação', widget= forms.Textarea)