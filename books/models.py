# https://blog.journalize.io/posts/an-elegant-db-schema-for-double-entry-accounting/

from django.db import models

# First elements (ie. 1 or -1) go into the database
balance_choices = ((1, 'credit'), (-1, 'debit'))


class Account(models.Model):
    
    name = models.CharField(max_length=255)
    number = models.IntegerField()
    normal = models.IntegerField(choices=balance_choices)
    
    def __str__(self):
        return str(self.number) + ' ' + self.name


class Transaction(models.Model):
    
    #identifies all single-entry items 
    # that make up a single transaction
    transaction_id = models.IntegerField()
    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    account = models.ForeignKey(Account, on_delete=models.RESTRICT)
    direction = models.IntegerField(choices=balance_choices)


