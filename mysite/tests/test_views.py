from django.test import TestCase, Client
from django.urls import reverse
from page.models import Service, Worker, Requests
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.appointment_url = reverse('appointment')
        self.ManageAppointment_url = reverse('ManageAppointment')

    def test_index_GET(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_appointment_GET(self):
        response = self.client.get(self.appointment_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'appointment.html')
