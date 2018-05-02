from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from .models import LegalText, SocialIdentities
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from django.http.response import HttpResponseRedirect
from AcmeExplorer.models import Actor, Ranger, Explorer, Manager, Administrator, Sponsor, Auditor,\
    Folder
from .forms import FolderForm, SocialIdentitiesForm
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist

adminP = Permission.objects.get_or_create(codename="ADMINISTRATOR", content_type=ContentType.objects.get_for_model(Administrator))
auditorP = Permission.objects.get_or_create(codename="AUDITOR", content_type=ContentType.objects.get_for_model(Auditor))
explorerP = Permission.objects.get_or_create(codename="EXPLORER", content_type=ContentType.objects.get_for_model(Explorer))
sponsorP = Permission.objects.get_or_create(codename="SPONSOR", content_type=ContentType.objects.get_for_model(Sponsor))
rangerP = Permission.objects.get_or_create(codename="RANGER", content_type=ContentType.objects.get_for_model(Ranger))
managerP = Permission.objects.get_or_create(codename="MANAGER", content_type=ContentType.objects.get_for_model(Manager))


# admin = Permission.objects.create(codename="ADMIN", name="Permission for admins", content_type=ContentType.objects.get(pk=34))
# sponsor = Permission.objects.create(codename="SPONSOR", name="Permission for sponsors")
# ranger = Permission.objects.create(codename="RANGER", name="Permission for rangers", content_type=ContentType.objects.get(pk=38))
# explorer = Permission.objects.create(codename="EXPLORER", name="Permission for explorers", content_type=ContentType.objects.get(pk=36))
# auditor = Permission.objects.create(codename="AUDITOR", name="Permission for auditors")
# manager = Permission.objects.create(codename="MANAGER", name="Permission for managers")

# Create your views here.
def home(request):
    return render(request,"base.html")

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
            ranger = Actor.create_user(self, datos['username'], datos['email'], datos['password'], datos['phoneNumber'], datos['address'], datos['first_name'],datos['last_name'])
            ranger.user_permissions.add(rangerP)
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
            explorer = Actor.create_user(self, datos['username'], datos['email'], datos['password'], datos['phoneNumber'], datos['address'], datos['first_name'],datos['last_name'])
            explorer.user_permissions.add(explorerP[0])
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
            admin = Actor.create_user(self, datos['username'], datos['email'], datos['password'], datos['phoneNumber'], datos['address'], datos['first_name'],datos['last_name'])
            admin.user_permissions.add(adminP)
            return HttpResponseRedirect('/AcmeExplorer/')
        else:
            return HttpResponseRedirect('/AcmeExplorer/admin/create', {"form":form})
    

#Esto solo los admins
class LegalTextCreate(CreateView):
    permission_required = 'ADMINISTRATOR'
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
    permission_required = 'ADMINISTRATOR'
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
    permission_required = 'ADMINISTRATOR'
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


class LegalTextList(ListView):
    permission_required = 'ADMINISTRATOR'
    model = LegalText
    template_name = "AcmeExplorer/legalText/legalText_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fields = [campo for campo in LegalText._meta.fields]
        campos = [fields[i].attname for i in range(0, len(fields))]
        lista = list(campos)
        lista.pop(0)
        context['fields'] = lista
        context['modelo'] = 'Legal Text'
        return context
        

#################################Social Identities#########################################
## Funciona
def socialIdentitiesCreate(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SocialIdentitiesForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            si = SocialIdentities()
            actor = Actor.objects.all().filter(pk=request.user.id).get()
            si.reconstruct(nick=form.cleaned_data['nick'], socialNetworkName=form.cleaned_data['socialNetworkName'], profileLink=form.cleaned_data['profileLink'], photo=form.cleaned_data['photo'], user=actor)
            si.save()
            pk = request.user.id
            return HttpResponseRedirect(reverse('AcmeExplorer:socialIdentitiesUserList', args=(pk, )))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SocialIdentitiesForm()

    return render(request, 'AcmeExplorer/socialIdentities/socialIdentities_form.html', {'form': form})


## Funciona
class SocialIdentitiesUpdate(UpdateView):
    model = SocialIdentities
    fields = ['nick','socialNetworkName','profileLink','photo']
    template_name = "AcmeExplorer/socialIdentities/socialIdentities_form.html"
    success_url = reverse_lazy('AcmeExplorer:socialIdentitiesList')
    
    def get(self, request, *args, **kwargs):
        if SocialIdentities.objects.get(pk=kwargs.get("pk")).user.id == request.user.id:
            return UpdateView.get(self, request, *args, **kwargs)
        else:
            return HttpResponseRedirect("/AcmeExplorer/")

## Funciona
class SocialIdentitiesDelete(DeleteView):
    model = SocialIdentities
    success_url = reverse_lazy('AcmeExplorer:socialIdentitiesList')
    
    def get(self, request, *args, **kwargs):
        if SocialIdentities.objects.get(pk=kwargs.get("pk")).user.id == request.user.id:
            return DeleteView.get(self, request, *args, **kwargs)
        else:
            return HttpResponseRedirect("/AcmeExplorer/")

## Funciona
class SocialIdentitiesDisplay(DetailView):
    model = SocialIdentities
    template_name = "AcmeExplorer/socialIdentities/socialIdentities_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = SocialIdentities._meta.get_fields()
        return context

## Funciona
class SocialIdentitiesList(ListView):
    model = SocialIdentities
    template_name = "AcmeExplorer/socialIdentities/socialIdentities_list.html"
    
    def get_context_data(self, **kwargs):
        #object_list = SocialIdentities.objects.get(user_id = userId)
        context = super().get_context_data(**kwargs)
        fields = [campo for campo in SocialIdentities._meta.fields]
        campos = [fields[i].attname for i in range(0, len(fields))]
        lista = list(campos)
        lista.pop(0)
        object_list = []
        try:
            #userIDS = SocialIdentities.objects.filter(user_=kwargs.get("user_pk"))
            object_list = SocialIdentities.objects.filter(user_id = self.request.user.id)
        except ObjectDoesNotExist:
            pass
        context['object_list'] = object_list
        context['fields'] = lista
        context['modelo'] = 'Legal Text'
        return context


#################################Folder#########################################
## Funciona
def folderCreate(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FolderForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            folder = Folder()
            actor = Actor.objects.all().filter(pk=request.user.id).get()
            folder.reconstruct(name=form.cleaned_data['name'], systemFolder=form.cleaned_data['systemFolder'], user=actor, parentFolder=form.cleaned_data['parentFolder'])
            folder.save()
            return HttpResponseRedirect(reverse_lazy('AcmeExplorer:folderList', ))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FolderForm()
        form.fields['parentFolder'].queryset = Folder.objects.filter(user_id = request.user.id)

    return render(request, 'AcmeExplorer/folder/folder_form.html', {'form': form})

## Funciona
def folderUpdate(request, pk):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FolderForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            folder = Folder()
            actor = Actor.objects.all().filter(pk=request.user.id).get()
            folder.reconstruct(name=form.cleaned_data['name'], systemFolder=form.cleaned_data['systemFolder'], user=actor, parentFolder=form.cleaned_data['parentFolder'])
            folder.save()
            return HttpResponseRedirect(reverse_lazy('AcmeExplorer:folderList', ))

    # if a GET (or any other method) we'll create a blank form
    else:
        folderUpdated = Folder.objects.filter(pk=pk).get()
        form = FolderForm(instance = folderUpdated)
        form.fields['parentFolder'].queryset = Folder.objects.filter(user_id = request.user.id)

    return render(request, 'AcmeExplorer/folder/folder_form.html', {'form': form})

## Funciona
class FolderDelete(DeleteView):
    model = Folder
    success_url = reverse_lazy('AcmeExplorer:folderList')
    next = reverse_lazy('AcmeExplorer:folderList')
    
    def post(self, request, *args, **kwargs):
        if Folder.objects.get(pk=kwargs.get("pk")).user.id == request.user.id and Folder.objects.get(pk=kwargs.get("pk")).systemFolder == False:
            return DeleteView.post(self, request, *args, **kwargs)
        else:
            return HttpResponseRedirect("/AcmeExplorer/folder/"+str(kwargs.get("pk")))

## Funciona
class FolderDisplay(DetailView):
    model = Folder
    template_name = "AcmeExplorer/folder/folder_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = Folder._meta.get_fields()
        return context

## Funciona
class FolderList(ListView):
    model = Folder
    template_name = "AcmeExplorer/folder/folder_list.html"
    
    def get_context_data(self, **kwargs):
        #object_list = SocialIdentities.objects.get(user_id = userId)
        context = super().get_context_data(**kwargs)
        fields = [campo for campo in Folder._meta.fields]
        campos = [fields[i].attname for i in range(0, len(fields))]
        lista = list(campos)
        lista.pop(0)
        object_list = []
        try:
            #userIDS = SocialIdentities.objects.filter(user_=kwargs.get("user_pk"))
            object_list = Folder.objects.filter(user_id = self.request.user.id)
        except ObjectDoesNotExist:
            pass
        context['object_list'] = object_list
        context['fields'] = lista
        context['modelo'] = 'Legal Text'
        return context