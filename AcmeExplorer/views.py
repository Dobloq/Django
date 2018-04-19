from django.shortcuts import render
from django.urls import reverse_lazy
from AcmeExplorer.models import LegalText
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

# Create your views here.
def home(request):
    return render(request,"base.html", {"nombre":"Manolo", "rol":"admin"})

# def createRanger(request):
#     errors = []
#     if request.method == 'POST':
#         if not request.POST["first_name"]:
#             errors.append('Introduce tu nombre')
#         if not request.POST["last_name"]:
#             errors.append("Introduce tus apellidos")
#         if not request.POST["username"]:
#             errors.append("Introduce tu nombre de usuario")
#         if not request.POST["password"]:
#             errors.append("Introduce tu contrasena")
#         if not request.POST["email"]:
#             errors.append("Introduce tu correo electronico")
# #         if not request.POST["password"].__eq(request.POST["repeatPassword"]):
# #             errors.append("Las contrasenas no coinciden")
#         if not errors:
#             user =Ranger.objects.create_user(request.POST["username"], request.POST["email"], request.POST["password"])
#             user.save()
#         return home(request)
#     else:
#         form = FormRanger
#         return render(request,"form.html", {"form":form})

class LegalTextCreate(CreateView):
    model = LegalText
    fields = ['title','body','applicableLaws','draftMode']
    success_url = reverse_lazy('AcmeExplorer:legalTextList')
    template_name = "AcmeExplorer/legalText/legalText_form.html"

class LegalTextUpdate(UpdateView):
    model = LegalText
    fields = ['id','title','body','applicableLaws','draftMode']
    template_name = "AcmeExplorer/legalText/legalText_form.html"
    success_url = reverse_lazy('AcmeExplorer:legalTextList')

class LegalTextDelete(DeleteView):
    model = LegalText
    success_url = reverse_lazy('AcmeExplorer:legalTextList')

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

#first_name, last_name, phoneNumber = None, address = None, username, email, password
