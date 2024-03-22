from django.shortcuts import render,redirect
from .models import Service,Requests, Worker
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template

def index(request):
    servs = Service.objects.all()
    workers = Worker.objects.all()
    count = Requests.objects.filter(Accepted=False).count()
    return render(request, 'index.html', {'servs' : servs, 'count' : count, 'workers' : workers})

def appointment(request):
    servs = Service.objects.all()
    if request.method=='POST':
        last_name1=request.POST.get('last_name1')
        first_name1 = request.POST.get('first_name1')
        surname = request.POST.get('surname')
        email3 = request.POST.get('email3')
        mobile = request.POST.get('mobile')
        Request = request.POST.get('Request')

        app = Requests.objects.create(
            Last_name = last_name1,
            First_name = first_name1,
            Patronymic = surname,
            Email = email3,
            Phone = mobile,
            Request = Request
        )
        app.save();
        messages.warning(request, 'Заявка отправлена, ожидайте ответа')
        return redirect('/')
    else:
        return render(request, "appointment.html", {'servs': servs})

def ManageAppointment(request):
    apps = Requests.objects.all()
    paginator = Paginator(apps, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.user.is_staff:
        return render(request, "manage-appointments.html", {'apps': apps, 'page_obj' : page_obj})
    else:
        return redirect('/')

def SendEmail(request):
    name=request.POST['name']
    email2=request.POST['email2']
    message2=request.POST['message2']

    email=EmailMessage(
        subject=f"Входящее письмо от {name}",
        body=message2,
        from_email= settings.EMAIL_HOST_USER,
        to=[settings.EMAIL_HOST_USER],
        reply_to=[email2]
    )
    email.send()
    messages.warning(request, 'Ваше письмо успешно отправлено')
    return redirect('index')

def Accepting(request):
    date = request.POST['date']
    abc_id = request.POST['appointment-id']
    abc = Requests.objects.get(id=abc_id)
    abc.Accepted = True
    abc.Accepted_date = datetime.datetime.now()
    abc.save()

    data = {
        'acc_name': abc.First_name,
        'date': date
    }

    message = get_template('email.html').render(data)
    email = EmailMessage(
        subject="Ваша заявка одобрена",
        body=message,
        from_email=settings.EMAIL_HOST_USER,
        to=[abc.Email]
    )
    email.content_subtype = "html"
    email.send()
    return redirect('ManageAppointment')

def Declining(request):
    abc_id = request.POST['appointment-id']
    abc = Requests.objects.get(id=abc_id)
    abc.Accepted = False
    abc.Accepted_date = datetime.datetime.now()
    abc.save()

    email = EmailMessage(
        subject="Ваша заявка отменена",
        body="Для того, чтобы узнать причину, пожалуйста, свяжитесь с нами",
        from_email=settings.EMAIL_HOST_USER,
        to=[abc.Email]
    )
    email.content_subtype = "html"
    email.send()
    return redirect('ManageAppointment')

def DeleteRequest(request):
    abc_id = request.POST['appointment-id']
    abc = Requests.objects.get(id=abc_id)

    email = EmailMessage(
        subject="Ваша заявка отклонена",
        body="К сожалению, наша компания не сможет предоставить Вам свои услуги. "
             "Для получения дополнительной информации, пожалуйста, свяжитесь с нами",
        from_email=settings.EMAIL_HOST_USER,
        to=[abc.Email]
    )
    email.content_subtype = "html"
    email.send()
    Requests.objects.filter(id=abc_id).delete()
    return redirect('ManageAppointment')