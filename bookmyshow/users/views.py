from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic 
from .forms import CustomUserCreationForm

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def city(request):
    return render(request,'users/city.html')
def hyd(request):
    return render(request,'users/hydhome.html')
def delhi(request):
    return render(request,'users/delhihome.html')
def bang(request):
    return render(request,'users/banghome.html')
def toystory(request):
    return render(request,'users/toystory.html')
def toystory_tickets(request):
    return render(request,'users/toystory_tickets.html')
def ohbaby(request):
    return render(request,'users/ohbaby.html')
def ohbaby_tickets(request):
    return render(request,'users/ohbaby_tickets.html')
def kabir(request):
    return render(request,'users/kabir.html')
def kabir_tickets(request):
    return render(request,'users/kabir_tickets.html')
def anna(request):
    return render(request,'users/anna.html')
def anna_tickets(request):
    return render(request,'users/anna_tickets.html')
def a15(request):
    return render(request,'users/a15.html')
def a15_tickets(request):
    return render(request,'users/a15_tickets.html')
def bro(request):
    return render(request,'users/bro.html')
def bro_tickets(request):
    return render(request,'users/bro_tickets.html')
def seats(request):
    return render(request,'users/seats.html')
def seats1(request):
    return render(request,'users/seats1.html')
def seats2(request):
    return render(request,'users/seats2.html')
def tickit(request):
    return render(request,'users/tickit.html')
def search(request):
    return render(request,'users/search.html')
def ticket(request):
    return render(request,'users/ticket.html')

# Create your views here.
