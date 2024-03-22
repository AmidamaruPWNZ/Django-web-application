from django.test import SimpleTestCase
from django.urls import resolve, reverse
from page.views import index, appointment, ManageAppointment, Accepting, Declining, DeleteRequest, SendEmail


class TestUrls(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_appointment_url_is_resolved(self):
        url = reverse('appointment')
        self.assertEquals(resolve(url).func, appointment)

    def test_ManageAppointment_url_is_resolved(self):
        url = reverse('ManageAppointment')
        self.assertEquals(resolve(url).func, ManageAppointment)

    def test_Accepting_url_is_resolved(self):
        url = reverse('Accepting')
        self.assertEquals(resolve(url).func, Accepting)

    def test_Declining_url_is_resolved(self):
        url = reverse('Declining')
        self.assertEquals(resolve(url).func, Declining)

    def test_DeleteRequest_url_is_resolved(self):
        url = reverse('DeleteRequest')
        self.assertEquals(resolve(url).func, DeleteRequest)

    def test_SendEmail_url_is_resolved(self):
        url = reverse('SendEmail')
        self.assertEquals(resolve(url).func, SendEmail)