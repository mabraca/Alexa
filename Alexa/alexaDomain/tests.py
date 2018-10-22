from django.test import TestCase
from .models import *
from django.db import transaction, IntegrityError
from django.contrib.auth.models import User

class UserTestCase(TestCase):
    
    def setUp(self):
        self.regUser = User.objects.create( username = 'RegularTestCaseUser', password= '123456Prueba' )
        
        self.url = recentViews.objects.create(url="https://www.alexa.com/topsites")
        
    def test_integrity_on_create(self):
        try:
            with transaction.atomic():
                asd = User.objects.create(
                    username = self.regUser.username,
                    password= '123456Prueba'
                )
            self.fail('Integrity net boing checked propperly at User name')
        except IntegrityError:
            pass
        try:
            with transaction.atomic():
                asd = recentViews.objects.create(
                    url = self.url.url
                )
            self.fail('Integrity net boing checked propperly at url ')
        except IntegrityError:
            pass
            
        try:
            with transaction.atomic():
                asd = User.objects.create(
                    username = 'NewUser',
                    password = None
                )
            self.fail('Password could not be empty')
        except IntegrityError:
            pass

        

# Create your tests here.
