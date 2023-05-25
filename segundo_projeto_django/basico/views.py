from django.shortcuts import render
from basico.reserva_form import ReservaForms
""" 
A função reserva irá, numa requisição post,validadas as informações, retornar a página com uma mensagem
de sucesso. Se a requisição for get a mesma retorna um formulário vazio.
"""
def reserva(requests):
   
   contexto ={'sucesso':False}
   if requests.method == "POST":
      formulario = ReservaForms(requests.POST)
      contexto['sucesso'] = True
   else:
      formulario = ReservaForms()

   contexto['formulario'] = formulario

   return render(requests,'reserva_pet.html',contexto)



   