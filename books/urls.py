from django.urls import path
from books.views import TransactionListView, TransactionDeleteView, TransactionUpdateView, TransactionCreateView


urlpatterns = [
    path('', TransactionListView.as_view(), name='ledger'),
    path('create/', TransactionCreateView.as_view(), name='transaction_create'),
    path('<pk>/update/', TransactionUpdateView.as_view(), name='transaction_update'),
    path('<pk>/delete/', TransactionDeleteView.as_view(), name='transaction_delete'),
]