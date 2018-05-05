from django.test import TestCase, Client
from django import setup
import AcmeExplorer

# Create your tests here.

class LegalTextTest(TestCase):
    
    def setUp(self):
        self.client = Client
        print("tuputamadre")
    
    def test_list(self):
        self.client.login(username="mineralnatural", password="mineralnatural")
        self.assertDictEqual(self.client.get(   "/AcmeExplorer/legalText"), AcmeExplorer.models.LegalText.objects.all(), "Coindiden")