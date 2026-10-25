from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import TicketForm
from .models import ticket


@login_required
def lista_tickets(request):
    tickets = ticket.objects.order_by('-fechacreacion')
    form = TicketForm()
    return render(request, 'lista_tickets.html', {'tickets': tickets, 'form': form})

def crear_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket_obj = form.save(commit=False)
            ticket_obj.usuario = request.user
            ticket_obj.save()
            return redirect('listar_tickets')
        tickets = ticket.objects.order_by('-fechacreacion')
        return render(request, 'lista_tickets.html', {'tickets': tickets, 'form': form})

    return redirect('listar_tickets')

def editar_ticket(request, pk):
    ticket_obj = ticket.objects.get(idticket=pk)

    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket_obj)
        if form.is_valid():
            form.save()
            return redirect('listar_tickets')
        tickets = ticket.objects.order_by('-fechacreacion')
        return render(request, 'lista_tickets.html', {'tickets': tickets, 'form': form})

    form = TicketForm(instance=ticket_obj)
    return render(request, 'lista_tickets.html', {'tickets': ticket.objects.order_by('-fechacreacion'), 'form': form})

def eliminar_ticket(request, pk):
    if request.method != 'POST':
        return redirect('listar_tickets')

    ticket_obj = get_object_or_404(ticket, idticket=pk)
    ticket_obj.eliminar_logico()
    return redirect('listar_tickets')