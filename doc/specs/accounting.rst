.. _spec-accounting:

Accounting
----------

A dedicated Django application provides the basic logic to store
accounting transactions. It provides some glue to make it easy
create and store such transactions from the various services.

Accounting basics
^^^^^^^^^^^^^^^^^
The application implements typical double-entry accounting. Each
transaction is defined by credit/debit operations over multiple
accounts and the sum of credits must be equal to the sum of debits.
When this is not the case, it should not be possible to store the
transaction.

You can add new transactions but never modify or delete past
transactions (this should even be enforceable at the database
level if we wanted).

There are 4 main types of accounts:

* Assets: Things you own (cash, stocks)
* Liabilities: Things you owe (debts)
* Revenue: Income (through sales)
* Expenses: Costs incurred for business

Here are some sample transactions from the point of view
of Freexian:

Sale of a 10 EUR book of Freexian with VAT

=========================  =====  ======
Accounts                   Debit  Credit
=========================  =====  ======
Paypal Account (Asset)     9.18
Paypal Fee (Expense)       0.82
VAT collected (Liability)         1.64
Sales of book (Revenue)           8.36
=========================  =====  ======

Sale of a book by a Librement user Joe from the point of view of Freexian:

=========================  =====  ======
Accounts                   Debit  Credit
=========================  =====  ======
Paypal Account (Asset)     9.18
Librement Fee (Revenue)           1.00
User Joe (Liabilily)              8.18
=========================  =====  ======

Same sale from the point of view of the user (without VAT):

=========================  =====  ======
Accounts                   Debit  Credit
=========================  =====  ======
Librement Account (Asset)  8.18
Paypal Fee (Expense)       0.82
Librement Fee (Expense)    1.00
Sales of book (Revenue)           10.00
=========================  =====  ======

Misc requirements
^^^^^^^^^^^^^^^^^
It should be relatively easy to tweak the logic of the accounting as
accounting rules tend to change over time. Changing the logic should not
have any effect on already recorded transactions.

Django data model
^^^^^^^^^^^^^^^^^
The application should support an arbitrary number of accounting books. An
accounting book is just a way to group together related accounting
transactions/records. Each accounting book has its own chart of accounts
and has a slug (symbolic name that is unique).

Each account is specified by:

* a unique internal identifier (unique across all accounting books)
* its parent accounting book
* a user-customizable identifier
* a user-customizable textual description
* a type of account

  * equity
  * asset
  * liability
  * revenue
  * expense

* a currency to be imposed on all lines affecting this account
  (can be unset if the account can hold multiple currencies)
* an internal identifier which is unique when combined with the accounting
  book. This will be used by other objects to find out associated
  accounts (e.g. a Product will have Revenues accounts, Users will have
  Liabilities accounts, etc.)

Each transaction includes:

* a parent accounting book
* a timestamp
* a textual description
* a set of at least two entries

Each transaction entry is always part of a transaction and includes:

* an associated account (which must be part of the same book as the parent
  transaction)
* an amount of money (negative means debit, positive means credit)
* a currency
* an optional description

Having different currencies in the same transaction means that we're
recording a currency conversion. The default functions should assume that
we have the same currency in a transaction and currency conversion should
have a dedicated API (that doesn't impose the equality between debits and
credits, but that ensures that we're doing a conversion between two
assets accounts and maybe an expense accounts for conversion fees).

Django integration
^^^^^^^^^^^^^^^^^^

There must be a default accounting book associated to each Django Site.

Supplementary accounting books should be associated to other Django
objects. They should be documented in (the meta-information of) their
Model and auto-created.

It should also be possible to define default accounts that should be
created automatically. All this must happen via with the help
of (multiple) inheritance on a specific model which hooks into
django.db.models.signals.post_save to do its work transparently.

Usage example::

    from librement.accounting.models import AccountingMixin
    from librement.accounting.types import AccountTypes

    class User(AccountingMixin):

        # This attribute is auto-detected and filled at creation time
        ledger = models.ForeignKey(AccountingBook)

        class Meta:
            # Object IDentifier = prefix + ":" + primary key,
            # uses lower case model name by default
            accounting_oid_prefix = "user"
            # List of accounts to created by default
            accounting_default_accounts = (
                {
                    # Book not set, assuming site-wide accounting
                    'type': AccountTypes.LIABILITY,
                    'description': 'Librement account of %(objectdesc)s',
                    'id': 'liability:account:%(oid)'
                }, {
                    'book': '%(oid)s',
                    'type': AccountTypes.ASSET,
                    'description': 'Librement account',
                    'id': 'asset:account'
                }, {
                    'book': '%(oid)s',
                    'type': AccountTypes.EXPENSE,
                    'description': 'Librement fees',
                    'id': 'expense:librement-fees'
                }
            )

Administrative views
^^^^^^^^^^^^^^^^^^^^
Accounting data should be browseable and downloadable as CSV files.
The main view should be a balance over a configurable period of time
(by default the current month, with a quicklink to access the former
month).

A balance shows the sum of debits and credits over all accounts that
have been affected by a transaction over the given period of time. It's
the combination of all transactions in fact.

It should be possible to click on a given account and see all the lines
which affected the account over the given period of time. Since each line
is part of a transaction, it should be possible to click on the
transaction and see the full transaction.

.. note:: We need to find a clean way to restrict access so that only
   the admin can see site-wide accounting data and so that each user can
   only inspect accounting data in his own book. The answer probably
   involves django-guardian but it's not clear how exactly.
