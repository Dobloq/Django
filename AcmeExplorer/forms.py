'''
Created on 16 abr. 2018

@author: X2835
'''
from django import forms

class Formulario(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)