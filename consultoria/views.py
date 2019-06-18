from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.paginator import Paginator
from .models import Post, Service
from .forms import RegistrationForm, ContactForm
import logging
from django.contrib import messages

# Create your views here.
logger = logging.getLogger(__name__)


def deploy(request):
    return render(request, 'consultoria/skeleton.html', {})

def index(request):
    services = Service.objects.all()
    return render(request, 'consultoria/index.html', {'services':services})

def about(request):
    return render(request, 'consultoria/about.html', {})

def contacts(request):
    return render(request, 'consultoria/contacts.html', {})

def post_list(request):

    post_list = Post.objects.all().order_by('published_date')

    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 10)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'consultoria/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)


    return render(request, 'consultoria/post_detail.html', {'post':post})

def service_detail(request, pk):
    service = Service.objects.get(pk=pk)
    msg = "null";
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.service = service
            contact.save()
            msg = "Formulario enviado com sucesso, entraremos em contato em breve"
            form = ContactForm()
    else:
        form = ContactForm()

    return render(request, 'consultoria/service_detail.html', {'service':service, 'form':form, 'msg':msg})

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()


    else:
        form = RegistrationForm
        args = {'form':form}
        return render(request, 'consultoria/registration.html', args)

    return render(request, 'consultoria/contacts.html', {})
