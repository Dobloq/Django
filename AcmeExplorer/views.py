from django.shortcuts import render
from django.urls import reverse_lazy
from .models import LegalText, Administrator
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.http.response import HttpResponseRedirect
from AcmeExplorer.models import Actor, Ranger, Explorer
from django.contrib.auth.views import LogoutView, LoginView

# Create your views here.
def home(request):
    return render(request,"base.html", {"nombre":"Manolo", "rol":"admin"})

# class ActorCreate(CreateView):
#     model = Administrator
#     fields = ["first_name","last_name","username","password","email","phoneNumber","address"]
#     success_url = reverse_lazy('AcmeExplorer:home')
#     template_name = "AcmeExplorer/actor/actor_form.html"
#     
#     def post(self, request, *args, **kwargs):
#         form = self.get_form()
#         if form.is_valid():
#             datos = form.cleaned_data
#             Actor.create_user(self, datos['username'], datos['email'], datos['password'], datos['phoneNumber'], datos['address'], datos['first_name'],datos['last_name'])
#             return HttpResponseRedirect('/AcmeExplorer/')
#         else:
#             return HttpResponseRedirect('/AcmeExplorer/actor/create', {"form":form})
class Logout(LogoutView):
    next_page = "/AcmeExplorer/"
    
class Login(LoginView):
    next_page = "/AcmeExplorer/"

class RangerCreate(CreateView):
    model = Ranger
    fields = ["first_name","last_name","username","password","email","phoneNumber","address"]
    success_url = reverse_lazy('AcmeExplorer:home')
    template_name = "AcmeExplorer/ranger/ranger_form.html"
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            datos = form.cleaned_data
            Actor.create_user(self, datos['username'], datos['email'], datos['password'], datos['phoneNumber'], datos['address'], datos['first_name'],datos['last_name'])
            return HttpResponseRedirect('/AcmeExplorer/')
        else:
            return HttpResponseRedirect('/AcmeExplorer/ranger/create', {"form":form})
    
class ExplorerCreate(CreateView):
    model = Explorer
    fields = ["first_name","last_name","username","password","email","phoneNumber","address"]
    success_url = reverse_lazy('AcmeExplorer:home')
    template_name = "AcmeExplorer/explorer/explorer_form.html"
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            datos = form.cleaned_data
            Actor.create_user(self, datos['username'], datos['email'], datos['password'], datos['phoneNumber'], datos['address'], datos['first_name'],datos['last_name'])
            return HttpResponseRedirect('/AcmeExplorer/')
        else:
            return HttpResponseRedirect('/AcmeExplorer/explorer/create', {"form":form})
    
class AdminCreate(CreateView):
    model = Administrator
    fields = ["first_name","last_name","username","password","email","phoneNumber","address"]
    success_url = reverse_lazy('AcmeExplorer:home')
    template_name = "AcmeExplorer/admin/admin_form.html"
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            datos = form.cleaned_data
            Actor.superusuario(self, datos['username'], datos['email'], datos['password'], datos['phoneNumber'], datos['address'], datos['first_name'],datos['last_name'])
            return HttpResponseRedirect('/AcmeExplorer/')
        else:
            return HttpResponseRedirect('/AcmeExplorer/admin/create', {"form":form})
    

#Esto solo los admins
class LegalTextCreate(CreateView):
    model = LegalText
    fields = ['title','body','applicableLaws','draftMode']
    success_url = reverse_lazy('AcmeExplorer:legalTextList')
    template_name = "AcmeExplorer/legalText/legalText_form.html"
    
    def get(self, request, *args, **kwargs):
        u = request.user
        if isinstance(u, Administrator):
            return CreateView.get(self, request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/AcmeExplorer/')

#Esto solo los admins
class LegalTextUpdate(UpdateView):
    model = LegalText
    fields = ['id','title','body','applicableLaws','draftMode']
    template_name = "AcmeExplorer/legalText/legalText_form.html"
    success_url = reverse_lazy('AcmeExplorer:legalTextList')
    
    def get(self, request, *args, **kwargs):
        idL = kwargs.get('pk')
        l = LegalText
        l = l.objects.get(pk=idL)
        condicion = l.draftMode == False
        if not isinstance(request.user, Administrator):
            return HttpResponseRedirect('/AcmeExplorer/legalText/')
        elif condicion:
            return HttpResponseRedirect('/AcmeExplorer/')
        else:
            return UpdateView.get(self, request, *args, **kwargs)

#Solo los admins
class LegalTextDelete(DeleteView):
    model = LegalText
    success_url = reverse_lazy('AcmeExplorer:legalTextList')
    
    def get(self, request, *args, **kwargs):
        if isinstance(request.user, Administrator):
            return DeleteView.get(self, request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/AcmeExplorer/')

class LegalTextDisplay(DetailView):
    model = LegalText
    template_name = "AcmeExplorer/legalText/legalText_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = LegalText.getFields(LegalText)
        return context

#Solo los admins
class LegalTextList(ListView):
    model = LegalText
    template_name = "AcmeExplorer/legalText/legalText_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = LegalText.getFields(LegalText)
        context['modelo'] = 'Legal Text'
        return context
    
    def get(self, request, *args, **kwargs):
        if isinstance(request.user, Administrator):
            return ListView.get(self, request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/AcmeExplorer/')

#first_name, last_name, phoneNumber = None, address = None, username, email, password
