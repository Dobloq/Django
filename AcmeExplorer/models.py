from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Actor(User):
    pass

class SocialIdentities(models.Model):
    nick = models.CharField(max_length=40)
    socialNetworkName = models.CharField(max_length=40)
    profileLink = models.URLField(max_length=50)
    photo = models.URLField(max_length=50)
    user = models.ForeignKey(Actor, on_delete='CASCADE')


class Folder(models.Model):
    name = models.CharField(blank=False, max_length=12)
    systemFolder = models.BooleanField(blank=False, default=False)
    user = models.ForeignKey(Actor, on_delete='CASCADE')
    parentFolder = models.ForeignKey('self', on_delete='CASCADE')


class Message(models.Model):
    sentDate = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(blank=False, max_length=12)
    body = models.CharField(blank=False, max_length=240)
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
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    phoneNumber = models.CharField(max_length=40)
    explorer = models.ForeignKey(Explorer, on_delete='CASCADE')

    
class LegalText(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField(max_length=240)
    applicableLaws = models.PositiveSmallIntegerField(blank=False)
    registrationDate = models.DateField(auto_now_add=True)
    draftMode = models.BooleanField(null = False)
    
    def getFields(self):
        return ('Title','Body','Applicable Laws','Registration Date','Draft Mode')

    def save(self, force_insert=False, force_update=False, using=None, 
        update_fields=None):
        print(self.pk)
        if self.pk is not None:
            force_update = True
        return models.Model.save(self, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
    
class Category(models.Model):
    name = models.CharField(max_length=40)
    categories = models.ForeignKey('self', on_delete='CASCADE')

        
class Trip(models.Model):
    ticker = models.CharField(unique=True, max_length=12)
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=240)
    # price, derivada del precio de los stages
    requirements = models.TextField(blank=True, max_length=240)
    publicationDate = models.DateField
    startDate = models.DateField
    endDate = models.DateField
    cancelationReasons = models.TextField(blank=True, max_length = 240)
    category = models.ForeignKey(Category, on_delete='CASCADE')
    legalText = models.ForeignKey(LegalText, on_delete='PROTECT')

    
class Ranger(Actor):
    permission = 'RANGER'

    
class Curriculum(models.Model):
    ticker = models.CharField(unique=True, max_length=12)
    ranger = models.ForeignKey(Ranger, on_delete='CASCADE')


class PersonalRecord(models.Model):
    name = models.CharField(max_length=40)
    photo = models.URLField(max_length=50)
    email = models.EmailField(max_length=50)
    phoneNumber = models.CharField(('phone number'), blank=True, max_length=12)
    linkedInProfile = models.URLField(max_length=50)
    curriculum = models.ForeignKey(Curriculum, on_delete='CASCADE')

    
class EducationalRecord(models.Model):
    diplomaTitle = models.CharField(max_length=40)
    startDate = models.DateField
    endDate = models.DateField
    institution = models.CharField(max_length=40)
    attachment = models.URLField(blank=True)
    comments = models.TextField(blank=True, max_length = 240)
    curriculum = models.ForeignKey(Curriculum, on_delete='CASCADE')

    
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
    curriculum = models.ForeignKey(Curriculum, on_delete='CASCADE')

    
class MiscellaneousRecord(models.Model):
    title = models.CharField(max_length=40)
    attachment = models.URLField(blank=True)
    comments = models.TextField(blank=True, max_length=240)
    curriculum = models.ForeignKey(Curriculum, on_delete='CASCADE')


class Finder(models.Model):
    keyword = models.CharField(blank=True, max_length=12)
    minimumPrice = models.DecimalField(decimal_places=2, max_digits=6, null = True)
    maximumPrice = models.DecimalField(decimal_places=2, max_digits=6, null = True)
    minimumDate = models.DateField(null = True)
    maximimDate = models.DateField(null = True)
    results = models.ManyToManyField(Trip)
    lastUse = models.DateTimeField(auto_now_add=True, null = True)
    explorer = models.ForeignKey(Explorer, on_delete='CASCADE')

    
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
    comments = models.TextField(blank=True,max_length=240)
    rejectedReasons = models.TextField(blank=True,max_length = 240)
    creditCard = models.ForeignKey(CreditCard, on_delete='CASCADE')
    explorer = models.ForeignKey(Explorer, on_delete='CASCADE')
    trip = models.ForeignKey(Trip, on_delete='CASCADE')


class Audit(models.Model):
    momentOfCreation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=240)
    attachment = models.CharField(blank=True, max_length=50)
    finalMode = models.BooleanField(default=False)
    auditor = models.ForeignKey(Auditor, on_delete='CASCADE')
    trip = models.ForeignKey(Trip, on_delete='CASCADE')

    
class Note(models.Model):
    momentOfCreation = models.DateTimeField(auto_now_add=True)
    remark = models.CharField(max_length=40)
    reply = models.CharField(blank=True, max_length=240)
    momentOfReply = models.DateTimeField(blank=True)
    auditor = models.ForeignKey(Auditor, on_delete='CASCADE')
    trip = models.ForeignKey(Trip, on_delete='CASCADE')

    
class Sponsorship(models.Model):
    banner = models.URLField(max_length=50)
    additionalInfo = models.URLField(max_length=50)
    creditCard = models.ForeignKey(CreditCard, on_delete='SET_NULL')
    sponsor = models.ForeignKey(Sponsor, on_delete='CASCADE')
    trip = models.ForeignKey(Trip, on_delete='CASCADE')


class SurvivalClass(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=240)
    organizationMoment = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete='CASCADE')
    manager = models.ForeignKey(Manager, on_delete='CASCADE')
    trip = models.ForeignKey(Trip, on_delete='CASCADE')

    
class Story(models.Model):
    title = models.CharField(max_length=40)
    pieceOfText = models.TextField(max_length=240)
    attachments = models.TextField(blank=True, max_length=240)
    explorer = models.ForeignKey(Explorer, on_delete='CASCADE')
    trip = models.ForeignKey(Trip, on_delete='CASCADE')


class Stage(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=240)
    price = models.DecimalField
    trip = models.ForeignKey(Trip, on_delete='CASCADE')

    
class Tag(models.Model):
    name = models.CharField(max_length=40)


class TagValue(models.Model):
    value = models.CharField(max_length=40)
    trip = models.ForeignKey(Trip, on_delete='CASCADE')
    tag = models.ForeignKey(Tag, on_delete='CASCADE')