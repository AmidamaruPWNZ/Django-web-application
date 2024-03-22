from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('appointment', views.appointment, name='appointment'),
    path('ManageAppointment', views.ManageAppointment, name='ManageAppointment'),
    path('SendEmail', views.SendEmail, name='SendEmail'),
    path('Accepting', views.Accepting, name='Accepting'),
    path('Declining', views.Declining, name='Declining'),
    path('DeleteRequest', views.DeleteRequest, name='DeleteRequest')
]