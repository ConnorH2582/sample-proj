from django.test import TestCase

# Create your tests here.
from django.test import TestCase,Client
from contact_manager.models import Event, Contact
import unittest
#
class TestClient(unittest.TestCase):
    def setUp(self):
        self.client=Client()
        self.event = Event(name = 'New Event',date = '2016-01-01')
        self.contact = Contact(first_name = 'New',last_name = 'Contact',email = 'newcontact@email.com',phone = 1234567890,is_favorite=True)

    def tearDown(self):
        pass

    def test_event(self):
        self.assertEqual(self.event.name,'New Event')
        self.assertEqual(self.event.date,'2016-01-01')

    def test_contact(self):
        self.assertEqual(self.contact.first_name,'New')
        self.assertEqual(self.contact.last_name,'Contact')
        self.assertEqual(self.contact.email,'newcontact@email.com')
        self.assertIsInstance(self.contact.phone,int)
        self.assertEqual(self.contact.phone,1234567890)
        self.assertIsInstance(self.contact.is_favorite,bool)
        self.assertEqual(self.contact.is_favorite,True)

    def test_getIndexView(self):
        res = self.client.get('/contact_manager/')
        self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
    unittest.main()
