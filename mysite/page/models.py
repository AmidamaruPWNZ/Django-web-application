from django.db import models

class Service(models.Model):
    Service_name = models.CharField(max_length=100)
    Service_img = models.ImageField(upload_to='pics')
    Service_descr = models.TextField()
    Service_price = models.IntegerField()

class Worker(models.Model):
    Worker_First_name = models.CharField(max_length=50)
    Worker_Patronymic = models.CharField(max_length=50)
    Worker_Last_name = models.CharField(max_length=50)
    Worker_Position = models.CharField(max_length=100)
    Worker_img = models.ImageField(upload_to='pics')

class Requests(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Patronymic = models.CharField(max_length=50)
    Email = models.CharField(max_length=30)
    Phone = models.CharField(max_length=11)
    Request = models.TextField(blank=True)
    Sent_date = models.DateField(auto_now_add=True)
    Accepted = models.BooleanField(default=False)
    Accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.First_name

    class Meta:
        ordering = ["-Sent_date"]