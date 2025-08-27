from django.shortcuts import render, redirect
from django.conf import settings

API_KEY = settings.API_KEY

TOP_HEADLINES_URL = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
from News.models import *
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from datetime import datetime
currentdatatime=datetime.now().strftime("%d-%m-%Y %I-%M %p")
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from .forms import EmailForm


# Create your views here.
import requests
def index(request):
    url = f'https://newsapi.org/v2/top-headlines?country=in&apiKey={API_KEY}'
    data = requests.get(url)
    response = data.json()
    articles = response['articles']
    context = {'articles':articles}
    return render(request,'index.html',context)


def category(request,name):
    url = f'https://newsapi.org/v2/top-headlines?category={name}&apiKey={API_KEY}'
    data = requests.get(url)
    response = data.json()
    articles = response['articles']
    context = {'articles':articles,'category':name}
    return render(request,'category.html',context)

def search(request):
    search_term = request.GET['search']
    url = f'https://newsapi.org/v2/everything?q={search_term}&apiKey={API_KEY}'
    data = requests.get(url)
    response = data.json()
    articles = response['articles']
    context = {'articles':articles,'search':search_term}
    return render(request,'search.html',context)

def signup(request):
    msg=""
    if request.method=="POST":
        rd=Details()
        rd.fullname=request.POST["fullname"]
        rd.mobilenumber=request.POST["mobilenumber"]
        rd.emailid=request.POST["emailid"]
        rd.password=request.POST["password"]
        rd.save()
        msg="Registerd Successfully"
    return render(request,'signup.html',{"msg":msg})

def login(request):
	msg=""
	if request.method=="POST":
		p_emailid=request.POST["emailid"]
		p_password=request.POST["password"]
		
		if Details.objects.filter(emailid=p_emailid,password=p_password).exists():

			request.session["emailid"]=p_emailid
			return render(request,"index.html")
		else:
			msg="Invalid Login Details"
	return render(request,"login.html",{"msg":msg})


def notes(request):
      msg=""
      if request.method=="POST":   
        nd=Notes()
        nd.fullname=request.POST.get("fullname","")
        nd.subject=request.POST.get("subject","") 
        nd.save()
        msg="Notes Added" 
      return render(request,"notes.html")


def viewnotes(request):
	msg=""
    
	if request.method=="POST":
		subject=request.POST["subject"]
		Notes.objects.filter(subject=subject).delete()
		msg="Record Deleted Successfully"
	notesdata=Notes.objects.all()
	return render(request,"viewnotes.html",{"notesdata":notesdata, "msg":msg})

def viewnote(request):
	msg="" 
	if request.method=="POST":
		subject=request.POST["subject"]
		Notes.objects.filter(subject=subject).delete()
		msg="Record Deleted Successfully"
	notesdata=Notes.objects.all()     
	return render(request,"viewnote.html",{"notesdata":notesdata, "msg":msg})

def asignup(request):
    msg=""
    if request.method=="POST":
        rd=Details1()
        rd.fullname=request.POST["fullname"]
        rd.mobilenumber=request.POST["mobilenumber"]
        rd.emailid=request.POST["emailid"]
        rd.password=request.POST["password"]
        rd.save()
        msg="Registerd Successfully"
    return render(request,'asignup.html',{"msg":msg})

def alogin(request):
	msg=""
	if request.method=="POST":
		p_emailid=request.POST["emailid"]
		p_password=request.POST["password"]
		
		if Details1.objects.filter(emailid=p_emailid,password=p_password).exists():

			request.session["emailid"]=p_emailid
			return render(request,"asignup.html")
		else:
			msg="Invalid Login Details"
	return render(request,"alogin.html",{"msg":msg})

def email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            user_mail = settings.EMAIL_HOST_USER
            password = settings.EMAIL_HOST_PASSWORD
            receiver_mail = form.cleaned_data['receiver_mail']
            subject = form.cleaned_data['subject']
            email_text = form.cleaned_data['email_text']

            email = EmailMessage(
                subject=subject,
                body=email_text,
                from_email=user_mail,
                to=[receiver_mail]
            )
            email.send()
            return render(request, 'success.html', {'receiver_mail': receiver_mail})
    else:
        form = EmailForm()

    return render(request, 'email.html', {'form': form})

def imp_points(request):
      
      return render(request,"imp_points.html")

def uploadFile(request):
    if request.method == 'POST':
        filename = request.POST['filename']
        owner = request.POST['owner']
        pdf = request.FILES['pdf']
        cover = request.FILES['cover']

        a = Files(filename=filename, owner=owner, pdf=pdf, cover=cover)
        a.save()
        messages.success(request, 'File Submitted successfully!')
        return redirect('files')
    
       


class PelconView(generic.ListView):
	model = Pelcon
	template_name = 'pelcon.html'
	context_object_name = 'files'
	paginate_by = 4


	def get_queryset(self):

		return Pelcon.objects.order_by('-id')
      
def myUpload(request):
	return render(request, 'myupload.html')

def display(request):
	msg=""
	if request.method=="POST":
		mobilenumber=request.POST["mobilenumber"]
		Details.objects.filter(mobilenumber=mobilenumber).delete()
		msg="Record Deleted Successfully"
	data=Details.objects.all()
	return render(request, 'display.html',{"data":data})


def pelconUpload(request):
	if request.method == 'POST':
		name = request.POST['name']
		owner = request.POST['owner']
		pdf = request.FILES['pdf']
		

		a = Pelcon(name=name, owner=owner, pdf=pdf)
		a.save()
		messages.success(request, 'File Submitted successfully')
		return redirect('pelcon')
	else:
		messages.error(request, 'Files was not Submitted ')
		return redirect('myupload')

