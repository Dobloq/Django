"""DP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth.views import login, logout
from AcmeExplorer.views import home, LegalTextCreate, LegalTextUpdate, LegalTextList, LegalTextDisplay, LegalTextDelete, ExplorerCreate, RangerCreate, AdminCreate, Logout, Login

app_name = "AcmeExplorer"
urlpatterns = [
    path('', home, name="home"),
    path('logout/', Logout.as_view(), name="logout"),
    path('login/', Login.as_view(), name="login"),
#     path('ranger/nonauth/create', createRanger, name="createRanger"),
    path('legalText/create/', LegalTextCreate.as_view(), name="legalTextCreate"),
    path('legalText/<int:pk>/edit/', LegalTextUpdate.as_view(), name="legalTextUpdate"),
    path('legalText/<int:pk>/delete/', LegalTextDelete.as_view(), name="legalTextDelete"),
    path('legalText/<int:pk>/', LegalTextDisplay.as_view(), name="legalTextDisplay"),
    path('legalText/', LegalTextList.as_view(), name="legalTextList"),
    #path('actor/create/', ActorCreate.as_view(), name="actorCreate"),
    path('ranger/create/', RangerCreate.as_view(), name="rangerCreate"),
    path('explorer/create/', ExplorerCreate.as_view(), name="explorerCreate"),
    path('admin/create/', AdminCreate.as_view(), name="adminCreate"),
]
