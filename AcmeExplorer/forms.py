'''
Created on 16 abr. 2018

@author: X2835
'''
from django import forms
from .models import Folder, SocialIdentities, Message

class Formulario(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    
# class FormRanger(forms.ModelForm):
#     class Meta:
#         model = Ranger
#         fields = ["first_name","last_name","username","password","email"]
#         
    
# title = models.CharField
#     body = models.TextField
#     applicableLaws = models.PositiveSmallIntegerField
#     registrationDate = models.DateField(auto_now_add=True)
#     draftMode = models.BooleanField

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name', 'systemFolder', 'parentFolder']
        
class SocialIdentitiesForm(forms.ModelForm):
    class Meta:
        model = SocialIdentities
        fields = ['nick','socialNetworkName','profileLink','photo']
        
# sentDate, subject, body, priority, senderUser, receiverUser, folder
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject','body','priority','receiverUser']
        
class MessageBroadcastForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject','body','priority']