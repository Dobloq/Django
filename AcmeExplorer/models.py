from django.db import models
from django.contrib.auth.models import UserManager, BaseUserManager, User
from django.contrib.auth.hashers import make_password
from datetime import date
import random, string


# Create your models here.
class Actor(User, UserManager, BaseUserManager):
    phoneNumber = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=40, blank=True)
    
    def create_user(self, username, email, password, phoneNumber=None, address=None, first_name=None, last_name=None, **extra_fields):
        actor = self.model(username=username, email=email, phoneNumber=phoneNumber, address=address, first_name=first_name, last_name=last_name, **extra_fields)
        passwo = make_password(password)
        print(passwo)
        actor.set_password(password)
        actor.save()
        actor.createDefaultFolders()
        return actor
    
    def superusuario(self, username, email, password, phoneNumber=None, address=None, first_name=None, last_name=None):
        actor = Actor.create_user(self, username=username, email=email, password=password, phoneNumber=phoneNumber, address=address, first_name=first_name, last_name=last_name, is_staff = True, is_superuser = True)
        actor.createDefaultFolders()
        return actor
    
    @classmethod
    def normalize_username(cls, username):
        return super(Actor, cls).normalize_username(username)
    
    @classmethod
    def normalize_email(cls, email):
        return super(Actor, cls).normalize_email(email)
    
    def createDefaultFolders(self):
        folder1 = Folder()
        folder2 = Folder()
        folder3 = Folder()
        folder4 = Folder()
        folder5 = Folder()
        folder1.reconstruct("In box", True, self, None)
        folder2.reconstruct("Out box", True, self, None)
        folder3.reconstruct("Spam box", True, self, None)
        folder4.reconstruct("Notification box", True, self, None)
        folder5.reconstruct("Trash box", True, self, None)
        folder1.save()
        folder2.save()
        folder3.save()
        folder4.save()
        folder5.save()
        
        def __str__(self):
            return self.first_name + " " + self.last_name


class SocialIdentities(models.Model):
    nick = models.CharField(max_length=40)
    socialNetworkName = models.CharField(max_length=40)
    profileLink = models.URLField(max_length=50)
    photo = models.URLField(max_length=50)
    user = models.ForeignKey(Actor, on_delete=models.CASCADE)
    
    def reconstruct(self, nick, socialNetworkName, profileLink, photo, user):
        self.nick = nick
        self.socialNetworkName = socialNetworkName
        self.profileLink = profileLink
        self.photo = photo
        self.user = user
    

class Folder(models.Model):
    name = models.CharField(blank=False, max_length=20)
    systemFolder = models.BooleanField(blank=False, default=False)
    user = models.ForeignKey(Actor, on_delete=models.CASCADE)
    parentFolder = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    def reconstruct(self, name, systemFolder, user, parentFolder):
        self.name = name
        self.parentFolder = parentFolder
        self.user = user
        self.systemFolder = systemFolder


class Message(models.Model):
    sentDate = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(blank=False, max_length=12)
    body = models.CharField(blank=False, max_length=240)
    priority = models.CharField(choices=(('HIGH', 'HIGH'), ('NEUTRAL', 'NEUTRAL'), ('LOW', 'LOW')), max_length=12)
    senderUser = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='senderUser')
    receiverUser = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='receiverUser')
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    
    def reconstruct(self, subject, body, priority, senderUser, receiverUser, folder):
        self.subject = subject
        self.body = body
        self.priority = priority
        self.senderUser = senderUser
        self.receiverUser = receiverUser
        self.folder = folder

    
#     class Meta:
#         permissions = (("can_broadcast","Can broadcast a message"))
# 
#     
class Auditor(Actor):
    
    class Meta:
        permissions = (("AUDITOR","Permission for auditor"),)


class Administrator(Actor):
    
    class Meta:
        permissions = (("ADMINISTRATOR","Permission for administrator"),)


class Manager(Actor):
    
    class Meta:
        permissions = (("MANAGER","Permission for manager"),)


class Sponsor(Actor):
    
    class Meta:
        permissions = (("SPONSOR","Permission for sponsor"),)


class Explorer(Actor):
    
    class Meta:
        permissions = (("EXPLORER","Permission for explorer"),)


class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    phoneNumber = models.CharField(max_length=40)
    explorer = models.ForeignKey(Explorer, on_delete=models.CASCADE)
    
    def reconstruct(self, name, email, phoneNumber, explorer):
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber
        self.explorer = explorer

    
class LegalText(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField(max_length=240)
    applicableLaws = models.PositiveSmallIntegerField(blank=False)
    registrationDate = models.DateField(auto_now_add=True)
    draftMode = models.BooleanField(null=False)
    
    def getFields(self):
        return ('Title', 'Body', 'Applicable Laws', 'Registration Date', 'Draft Mode')

    
class Category(models.Model):
    name = models.CharField(max_length=40)
    parentCategory = models.ForeignKey('self', on_delete=models.CASCADE, blank = True, null = True)
    
    def __str__(self):
        return self.name

        
class Trip(models.Model):
    ticker = models.CharField(unique=True, max_length=12)
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=240)
    # price, derivada del precio de los stages
    requirements = models.TextField(blank=True, max_length=240)
    publicationDate = models.DateField
    startDate = models.DateField
    endDate = models.DateField
    cancelationReasons = models.TextField(blank=True, max_length=240)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    legalText = models.ForeignKey(LegalText, on_delete='PROTECT')

    
class Ranger(Actor):
    
    class Meta:
        permissions = (("RANGER","Permission for ranger"),)

    
class Curriculum(models.Model):
    ticker = models.CharField(unique=True, max_length=12)
    ranger = models.ForeignKey(Ranger, on_delete=models.CASCADE)


class PersonalRecord(models.Model):
    name = models.CharField(max_length=40)
    photo = models.URLField(max_length=50)
    email = models.EmailField(max_length=50)
    phoneNumber = models.CharField(('phone number'), blank=True, max_length=12)
    linkedInProfile = models.URLField(max_length=50)
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)

    
class EducationalRecord(models.Model):
    diplomaTitle = models.CharField(max_length=40)
    startDate = models.DateField
    endDate = models.DateField
    institution = models.CharField(max_length=40)
    attachment = models.URLField(blank=True)
    comments = models.TextField(blank=True, max_length=240)
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)

    
class ProfessionalRecord(models.Model):
    companyName = models.CharField(max_length=40)
    startDate = models.DateField
    endDate = models.DateField
    attachment = models.URLField(blank=True)
    role = models.CharField(max_length=40)
    comments = models.TextField(blank=True, max_length=240)


class EndorserRecord(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    phoneNumber = models.CharField(max_length=40)
    linkedInProfile = models.URLField(max_length=50)
    comments = models.TextField(blank=True, max_length=240)
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)

    
class MiscellaneousRecord(models.Model):
    title = models.CharField(max_length=40)
    attachment = models.URLField(blank=True)
    comments = models.TextField(blank=True, max_length=240)
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE)


class Finder(models.Model):
    keyword = models.CharField(blank=True, max_length=12)
    minimumPrice = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    maximumPrice = models.DecimalField(decimal_places=2, max_digits=6, null=True)
    minimumDate = models.DateField(null=True)
    maximimDate = models.DateField(null=True)
    results = models.ManyToManyField(Trip)
    lastUse = models.DateTimeField(auto_now_add=True, null=True)
    explorer = models.ForeignKey(Explorer, on_delete=models.CASCADE)

    
class CreditCard(models.Model):
    holderName = models.CharField(max_length=40)
    brandName = models.CharField(max_length=40)
    number = models.BigIntegerField
    expirationMonth = models.PositiveSmallIntegerField
    expirationYear = models.PositiveSmallIntegerField
    CVVCode = models.PositiveSmallIntegerField


class Location(models.Model):
    latitude = models.DecimalField(max_digits=2, decimal_places=2)
    longitude = models.DecimalField(max_digits=3, decimal_places=2)
    name = models.CharField(max_length=40)


class ConfigurationSystem(models.Model):
    spamWords = models.TextField(default='pennis, viagra, jes extender, cialis', max_length=240)
    defaultCountry = models.CharField(default='+34', max_length=4)
    tax = models.DecimalField(default=1.21, decimal_places=1, max_digits=3)
    timeResultsCached = models.PositiveSmallIntegerField(default=24)
    maxResults = models.PositiveSmallIntegerField(default=100)


class Application(models.Model):
    madeDate = models.DateField(auto_now_add=True)
    status = models.CharField(choices=(('DUE', 'DUE'), ('PENDING', 'PENDING'), ('REJECTED', 'REJECTED'), ('ACCEPTED', 'ACCEPTED'), ('CANCELLED', 'CANCELLED')), max_length=12)
    comments = models.TextField(blank=True, max_length=240)
    rejectedReasons = models.TextField(blank=True, max_length=240)
    creditCard = models.ForeignKey(CreditCard, on_delete=models.CASCADE)
    explorer = models.ForeignKey(Explorer, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)


class Audit(models.Model):
    momentOfCreation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=240)
    attachment = models.CharField(blank=True, max_length=50)
    finalMode = models.BooleanField(default=False)
    auditor = models.ForeignKey(Auditor, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

    
class Note(models.Model):
    momentOfCreation = models.DateTimeField(auto_now_add=True)
    remark = models.CharField(max_length=40)
    reply = models.CharField(blank=True, max_length=240)
    momentOfReply = models.DateTimeField(blank=True)
    auditor = models.ForeignKey(Auditor, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

    
class Sponsorship(models.Model):
    banner = models.URLField(max_length=50)
    additionalInfo = models.URLField(max_length=50)
    creditCard = models.ForeignKey(CreditCard, on_delete='SET_NULL')
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)


class SurvivalClass(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=240)
    organizationMoment = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

    
class Story(models.Model):
    title = models.CharField(max_length=40)
    pieceOfText = models.TextField(max_length=240)
    attachments = models.TextField(blank=True, max_length=240)
    explorer = models.ForeignKey(Explorer, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)


class Stage(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=240)
    price = models.DecimalField
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

    
class Tag(models.Model):
    name = models.CharField(max_length=40)


class TagValue(models.Model):
    value = models.CharField(max_length=40)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

def generarTicker():
    fecha = date.today().strftime("%y%m%d")
    letras = ""
    [letras+=random.choice(string.ascii_uppercase) for n in range(0,2)]
    ticker = fecha + "-" + letras
    return ticker