# Generated by Django 2.0.4 on 2018-04-19 12:16

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_auto_20180418_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('madeDate', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('DUE', 'DUE'), ('PENDING', 'PENDING'), ('REJECTED', 'REJECTED'), ('ACCEPTED', 'ACCEPTED'), ('CANCELLED', 'CANCELLED')], max_length=12)),
                ('comments', models.TextField(blank=True, max_length=240)),
                ('rejectedReasons', models.TextField(blank=True, max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('momentOfCreation', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=240)),
                ('attachment', models.CharField(blank=True, max_length=50)),
                ('finalMode', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('categories', models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ConfigurationSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spamWords', models.TextField(default='pennis, viagra, jes extender, cialis', max_length=240)),
                ('defaultCountry', models.CharField(default='+34', max_length=4)),
                ('tax', models.DecimalField(decimal_places=1, default=1.21, max_digits=3)),
                ('timeResultsCached', models.PositiveSmallIntegerField(default=24)),
                ('maxResults', models.PositiveSmallIntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('phoneNumber', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holderName', models.CharField(max_length=40)),
                ('brandName', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=12, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EducationalRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diplomaTitle', models.CharField(max_length=40)),
                ('institution', models.CharField(max_length=40)),
                ('attachment', models.URLField(blank=True)),
                ('comments', models.TextField(blank=True, max_length=240)),
                ('curriculum', models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Curriculum')),
            ],
        ),
        migrations.CreateModel(
            name='EndorserRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('phoneNumber', models.CharField(max_length=40)),
                ('linkedInProfile', models.URLField(max_length=50)),
                ('comments', models.TextField(blank=True, max_length=240)),
                ('curriculum', models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Curriculum')),
            ],
        ),
        migrations.CreateModel(
            name='Finder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(blank=True, max_length=12)),
                ('minimumPrice', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('maximumPrice', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('minimumDate', models.DateField(null=True)),
                ('maximimDate', models.DateField(null=True)),
                ('lastUse', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('systemFolder', models.BooleanField(default=False)),
                ('parentFolder', models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Folder')),
            ],
        ),
        migrations.CreateModel(
            name='LegalText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('body', models.TextField(max_length=240)),
                ('applicableLaws', models.PositiveSmallIntegerField()),
                ('registrationDate', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=2, max_digits=2)),
                ('longitude', models.DecimalField(decimal_places=2, max_digits=3)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentDate', models.DateTimeField(auto_now_add=True)),
                ('subject', models.CharField(max_length=12)),
                ('body', models.CharField(max_length=240)),
                ('priority', models.CharField(choices=[('HIGH', 'HIGH'), ('NEUTRAL', 'NEUTRAL'), ('LOW', 'LOW')], max_length=12)),
                ('folder', models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Folder')),
            ],
        ),
        migrations.CreateModel(
            name='MiscellaneousRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('attachment', models.URLField(blank=True)),
                ('comments', models.TextField(blank=True, max_length=240)),
                ('curriculum', models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Curriculum')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('momentOfCreation', models.DateTimeField(auto_now_add=True)),
                ('remark', models.CharField(max_length=40)),
                ('reply', models.CharField(blank=True, max_length=240)),
                ('momentOfReply', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('photo', models.URLField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phoneNumber', models.CharField(blank=True, max_length=12, verbose_name='phone number')),
                ('linkedInProfile', models.URLField(max_length=50)),
                ('curriculum', models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Curriculum')),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyName', models.CharField(max_length=40)),
                ('attachment', models.URLField(blank=True)),
                ('role', models.CharField(max_length=40)),
                ('comments', models.TextField(blank=True, max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name='SocialIdentities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=40)),
                ('socialNetworkName', models.CharField(max_length=40)),
                ('profileLink', models.URLField(max_length=50)),
                ('photo', models.URLField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsorship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.URLField(max_length=50)),
                ('additionalInfo', models.URLField(max_length=50)),
                ('creditCard', models.ForeignKey(on_delete='SET_NULL', to='AcmeExplorer.CreditCard')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('pieceOfText', models.TextField(max_length=240)),
                ('attachments', models.TextField(blank=True, max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name='SurvivalClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=240)),
                ('organizationMoment', models.DateTimeField(auto_now_add=True)),
                ('location', models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='TagValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=40)),
                ('tag', models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=12, unique=True)),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=240)),
                ('requirements', models.TextField(blank=True, max_length=240)),
                ('cancelationReasons', models.TextField(blank=True, max_length=240)),
                ('category', models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Category')),
                ('legalText', models.ForeignKey(on_delete='PROTECT', to='AcmeExplorer.LegalText')),
            ],
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('actor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='AcmeExplorer.Actor')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('AcmeExplorer.actor',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Auditor',
            fields=[
                ('actor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='AcmeExplorer.Actor')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('AcmeExplorer.actor',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Explorer',
            fields=[
                ('actor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='AcmeExplorer.Actor')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('AcmeExplorer.actor',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('actor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='AcmeExplorer.Actor')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('AcmeExplorer.actor',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Ranger',
            fields=[
                ('actor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='AcmeExplorer.Actor')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('AcmeExplorer.actor',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('actor_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='AcmeExplorer.Actor')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('AcmeExplorer.actor',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='tagvalue',
            name='trip',
            field=models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Trip'),
        ),
        migrations.AddField(
            model_name='survivalclass',
            name='trip',
            field=models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Trip'),
        ),
        migrations.AddField(
            model_name='story',
            name='trip',
            field=models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Trip'),
        ),
        migrations.AddField(
            model_name='stage',
            name='trip',
            field=models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Trip'),
        ),
        migrations.AddField(
            model_name='sponsorship',
            name='trip',
            field=models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Trip'),
        ),
        migrations.AddField(
            model_name='socialidentities',
            name='user',
            field=models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Actor'),
        ),
        migrations.AddField(
            model_name='note',
            name='trip',
            field=models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Trip'),
        ),
        migrations.AddField(
            model_name='message',
            name='receiverUser',
            field=models.ForeignKey(on_delete='CASCADE', related_name='receiverUser', to='AcmeExplorer.Actor'),
        ),
        migrations.AddField(
            model_name='message',
            name='senderUser',
            field=models.ForeignKey(on_delete='CASCADE', related_name='senderUser', to='AcmeExplorer.Actor'),
        ),
        migrations.AddField(
            model_name='folder',
            name='user',
            field=models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Actor'),
        ),
        migrations.AddField(
            model_name='finder',
            name='results',
            field=models.ManyToManyField(to='AcmeExplorer.Trip'),
        ),
        migrations.AddField(
            model_name='audit',
            name='trip',
            field=models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Trip'),
        ),
        migrations.AddField(
            model_name='application',
            name='creditCard',
            field=models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.CreditCard'),
        ),
        migrations.AddField(
            model_name='application',
            name='trip',
            field=models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Trip'),
        ),
        migrations.AddField(
            model_name='survivalclass',
            name='manager',
            field=models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Manager'),
        ),
        migrations.AddField(
            model_name='story',
            name='explorer',
            field=models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Explorer'),
        ),
        migrations.AddField(
            model_name='sponsorship',
            name='sponsor',
            field=models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Sponsor'),
        ),
        migrations.AddField(
            model_name='note',
            name='auditor',
            field=models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Auditor'),
        ),
        migrations.AddField(
            model_name='finder',
            name='explorer',
            field=models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Explorer'),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='ranger',
            field=models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Ranger'),
        ),
        migrations.AddField(
            model_name='contact',
            name='explorer',
            field=models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Explorer'),
        ),
        migrations.AddField(
            model_name='audit',
            name='auditor',
            field=models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Auditor'),
        ),
        migrations.AddField(
            model_name='application',
            name='explorer',
            field=models.ForeignKey(on_delete='CASCADE', to='AcmeExplorer.Explorer'),
        ),
    ]