from django.shortcuts import render, redirect
from .models import ticket
from .forms import TicketForm


def lista_tickets(request):
    tickets = ticket.objects.order_by('-fechacreacion')
    form = TicketForm()
    return render(request, 'lista_tickets.html', {'tickets': tickets, 'form': form})


def crear_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_tickets')
        else:
            tickets = ticket.objects.order_by('-fechacreacion')
            return render(request, 'lista_tickets.html', {'tickets': tickets, 'form': form})

    return redirect('listar_tickets')