from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Actor(User):
    permission = ''


class SocialIdentities(models.Model):
    nick = models.CharField
    socialNetworkName = models.CharField
    profileLink = models.URLField
    photo = models.URLField
    user = models.ForeignKey(Actor, on_delete='CASCADE')


class Folder(models.Model):
    name = models.CharField(blank=False, max_length=12)
    systemFolder = models.BooleanField(blank=False, default=False)
    user = models.ForeignKey(Actor, on_delete='CASCADE')
    parentFolder = models.ForeignKey('self', on_delete='CASCADE')


class Message(models.Model):
    sentDate = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(blank=False, max_length=12)
    body = models.CharField(blank=False, max_length=12)
    priority = models.CharField(choices=(('HIGH', 'HIGH'), ('NEUTRAL', 'NEUTRAL'), ('LOW', 'LOW')), max_length=12)
    senderUser = models.ForeignKey(Actor, on_delete='CASCADE', related_name='senderUser')
    receiverUser = models.ForeignKey(Actor, on_delete='CASCADE', related_name='receiverUser')
    folder = models.ForeignKey(Folder, on_delete='CASCADE')

    
class Auditor(Actor):
    permission = 'AUDITOR'


class Administrator(Actor):
    permission = 'ADMINISTRATOR'


class Manager(Actor):
    permission = 'MANAGER'


class Sponsor(Actor):
    permission = 'SPONSOR'


class Explorer(Actor):
    permission = 'EXPLORER'


class Contact(models.Model):
    name = models.CharField
    email = models.EmailField
    phoneNumber = models.CharField
    explorer = models.ForeignKey(Explorer, on_delete='CASCADE')

    
class LegalText(models.Model):
    title = models.CharField
    body = models.TextField
    applicableLaws = models.PositiveSmallIntegerField
    registrationDate = models.DateField(auto_now_add=True)
    draftMode = models.BooleanField

    
class Category(models.Model):
    name = models.CharField
    categories = models.ForeignKey('self', on_delete='CASCADE')

        
class Trip(models.Model):
    ticker = models.CharField(unique=True, max_length=12)
    title = models.CharField
    description = models.TextField
    # price, derivada del precio de los stages
    requirements = models.TextField(blank=True)
    publicationDate = models.DateField
    startDate = models.DateField
    endDate = models.DateField
    cancelationReasons = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete='CASCADE')
    legalText = models.ForeignKey(LegalText, on_delete='PROTECT')

    
class Ranger(Actor):
    permission = 'RANGER'

    
class Curriculum(models.Model):
    ticker = models.CharField(unique=True, max_length=12)
    ranger = models.ForeignKey(Ranger, on_delete='CASCADE')


class PersonalRecord(models.Model):
    name = models.CharField
    photo = models.URLField
    email = models.EmailField
    phoneNumber = models.CharField(('phone number'), blank=True, max_length=12)
    linkedInProfile = models.URLField
    curriculum = models.ForeignKey(Curriculum, on_delete='CASCADE')

    
class EducationalRecord(models.Model):
    diplomaTitle = models.CharField
    startDate = models.DateField
    endDate = models.DateField
    institution = models.CharField
    attachment = models.URLField(blank=True)
    comments = models.TextField(blank=True)
    curriculum = models.ForeignKey(Curriculum, on_delete='CASCADE')

    
class ProfessionalRecord(models.Model):
    companyName = models.CharField
    startDate = models.DateField
    endDate = models.DateField
    attachment = models.URLField(blank=True)
    role = models.CharField
    comments = models.TextField(blank=True)


class EndorserRecord(models.Model):
    name = models.CharField
    email = models.EmailField
    phoneNumber = models.CharField
    linkedInProfile = models.URLField
    comments = models.TextField(blank=True)
    curriculum = models.ForeignKey(Curriculum, on_delete='CASCADE')

    
class MiscellaneousRecord(models.Model):
    title = models.CharField
    attachment = models.URLField(blank=True)
    comments = models.TextField(blank=True)
    curriculum = models.ForeignKey(Curriculum, on_delete='CASCADE')


class Finder(models.Model):
    keyword = models.CharField(blank=True, max_length=12)
    minimumPrice = models.DecimalField(decimal_places=2, max_digits=6)
    maximumPrice = models.DecimalField(decimal_places=2, max_digits=6)
    minimumDate = models.DateField
    maximimDate = models.DateField
    results = models.ManyToManyField(Trip)
    lastUse = models.DateTimeField(auto_now_add=True)
    explorer = models.ForeignKey(Explorer, on_delete='CASCADE')

    
class CreditCard(models.Model):
    holderName = models.CharField
    brandName = models.CharField
    number = models.BigIntegerField
    expirationMonth = models.PositiveSmallIntegerField
    expirationYear = models.PositiveSmallIntegerField
    CVVCode = models.PositiveSmallIntegerField


class Location(models.Model):
    latitude = models.DecimalField(max_digits=2, decimal_places=2)
    longitude = models.DecimalField(max_digits=3, decimal_places=2)
    name = models.CharField


class ConfigurationSystem(models.Model):
    spamWords = models.TextField(default='pennis, viagra, jes extender, cialis')
    defaultCountry = models.CharField(default='+34', max_length=4)
    tax = models.DecimalField(default=1.21, decimal_places=1, max_digits=3)
    timeResultsCached = models.PositiveSmallIntegerField(default=24)
    maxResults = models.PositiveSmallIntegerField(default=100)


class Application(models.Model):
    madeDate = models.DateField(auto_now_add=True)
    status = models.CharField(choices=(('DUE', 'DUE'), ('PENDING', 'PENDING'), ('REJECTED', 'REJECTED'), ('ACCEPTED', 'ACCEPTED'), ('CANCELLED', 'CANCELLED')), max_length=12)
    comments = models.TextField(blank=True)
    rejectedReasons = models.TextField(blank=True)
    creditCard = models.ForeignKey(CreditCard, on_delete='CASCADE')
    explorer = models.ForeignKey(Explorer, on_delete='CASCADE')
    trip = models.ForeignKey(Trip, on_delete='CASCADE')


class Audit(models.Model):
    momentOfCreation = models.DateTimeField(auto_now_add=True)
    title = models.CharField
    description = models.TextField
    attachment = models.CharField(blank=True, max_length=50)
    finalMode = models.BooleanField
    auditor = models.ForeignKey(Auditor, on_delete='CASCADE')
    trip = models.ForeignKey(Trip, on_delete='CASCADE')

    
class Note(models.Model):
    momentOfCreation = models.DateTimeField(auto_now_add=True)
    remark = models.CharField
    reply = models.CharField(blank=True, max_length=240)
    momentOfReply = models.DateTimeField(blank=True)
    auditor = models.ForeignKey(Auditor, on_delete='CASCADE')
    trip = models.ForeignKey(Trip, on_delete='CASCADE')

    
class Sponsorship(models.Model):
    banner = models.URLField
    additionalInfo = models.URLField
    creditCard = models.ForeignKey(CreditCard, on_delete='SET_NULL')
    sponsor = models.ForeignKey(Sponsor, on_delete='CASCADE')
    trip = models.ForeignKey(Trip, on_delete='CASCADE')


class SurvivalClass(models.Model):
    title = models.CharField
    description = models.TextField
    organizationMoment = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete='CASCADE')
    manager = models.ForeignKey(Manager, on_delete='CASCADE')
    trip = models.ForeignKey(Trip, on_delete='CASCADE')

    
class Story(models.Model):
    title = models.CharField
    pieceOfText = models.TextField
    attachments = models.TextField(blank=True)
    explorer = models.ForeignKey(Explorer, on_delete='CASCADE')
    trip = models.ForeignKey(Trip, on_delete='CASCADE')


class Stage(models.Model):
    title = models.CharField
    description = models.TextField
    price = models.DecimalField
    trip = models.ForeignKey(Trip, on_delete='CASCADE')

    
class Tag(models.Model):
    name = models.CharField


class TagValue(models.Model):
    value = models.CharField
    trip = models.ForeignKey(Trip, on_delete='CASCADE')
    tag = models.ForeignKey(Tag, on_delete='CASCADE')
