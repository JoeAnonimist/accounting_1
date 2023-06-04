from django.shortcuts import render
from .models import Transaction
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView


def ledger(request):
    transaction_list = Transaction.objects.all()
    context = {'transaction_list': transaction_list}
    return render(request, 'books/ledger.html', context)


class TransactionListView(ListView):
    
    model = Transaction
    template_name = 'books/ledger.html'
    paginate_by = 100
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TransactionCreateView(CreateView):
    
    model = Transaction
    fields = ['transaction_id', 'date', 'amount', 'account', 'direction']
    success_url = '/'
    template_name = 'books/create.html'


class TransactionDeleteView(DeleteView):
    
    model = Transaction
    success_url = '/'
    template_name = 'books/delete.html'


class TransactionUpdateView(UpdateView):
    
    model = Transaction
    fields = ['date', 'amount', 'account', 'direction']
    success_url = '/'
    template_name = 'books/update.html'


