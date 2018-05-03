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
from AcmeExplorer.views import *

app_name = "AcmeExplorer"
urlpatterns = [
    path('', home, name="home"),
    path('logout/', Logout.as_view(), name="logout"),
    path('login/', Login.as_view(), name="login"),
#     path('ranger/nonauth/create', createRanger, name="createRanger"),

    ################################# Legal Text #########################################
    path('legalText/create/', LegalTextCreate.as_view(), name="legalTextCreate"),
    path('legalText/<int:pk>/edit/', LegalTextUpdate.as_view(), name="legalTextUpdate"),
    path('legalText/<int:pk>/delete/', LegalTextDelete.as_view(), name="legalTextDelete"),
    path('legalText/<int:pk>/', LegalTextDisplay.as_view(), name="legalTextDisplay"),
    path('legalText/', LegalTextList.as_view(), name="legalTextList"),
    
    ################################# Social Identities #########################################
    path('socialIdentities/<int:user_pk>/', SocialIdentitiesList.as_view(), name="socialIdentitiesUserList"),
    path('socialIdentities/', SocialIdentitiesList.as_view(), name="socialIdentitiesList"),
    path('socialIdentities/user/<int:pk>', SocialIdentitiesDisplay.as_view(), name="socialIdentitiesDisplay"),
    path('socialIdentities/user/<int:pk>/edit', SocialIdentitiesUpdate.as_view(), name="socialIdentitiesUpdate"),
    path('socialIdentities/user/<int:pk>/delete', SocialIdentitiesDelete.as_view(), name="socialIdentitiesDelete"),
    path('socialIdentities/create', socialIdentitiesCreate, name="socialIdentitiesCreate"),
    
    ################################# Folder #########################################
    path('folder/create', folderCreate, name="folderCreate"),
    path('folder/<int:pk>', FolderDisplay.as_view(), name="folderDisplay"),
    path('folder/', FolderList.as_view(), name="folderList"),
    path('folder/<int:pk>/edit', folderUpdate, name="folderUpdate"),
    path('folder/<int:pk>/delete', FolderDelete.as_view(), name="folderDelete"),
    
    ################################## Message ##############################################
    path('message/create', messageCreate, name="messageCreate"),
    path('message/<int:pk>', MessageDisplay.as_view(), name="messageDisplay"),
    path('message/', MessageList.as_view(), name="messageList"),
    path('message/<int:pk>/delete', MessageDelete.as_view(), name="messageDelete"),
    path('message/broadcast', messageBroadcast, name="messageBroadcast"),
    
    ################################## Contact #############################################33
    path('contact/create', contactCreate, name="contactCreate"),
    path('contact/<int:pk>', ContactDisplay.as_view(), name="contactDisplay"),
    path('contact/', ContactList.as_view(), name="contactList"),
    path('contact/<int:pk>/edit', contactUpdate, name="contactUpdate"),
    path('contact/<int:pk>/delete', ContactDelete.as_view(), name="contactDelete"),
    
    #path('actor/create/', ActorCreate.as_view(), name="actorCreate"),
    path('ranger/create/', RangerCreate.as_view(), name="rangerCreate"),
    path('explorer/create/', ExplorerCreate.as_view(), name="explorerCreate"),
    path('admin/create/', AdminCreate.as_view(), name="adminCreate"),
]
