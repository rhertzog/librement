Overview
========

The librement project aims to provide multiple services to free software
authors and users. The ultimate goal of all those services is to fund the
work of the free software authors (either directly or through their
respective project).

All those services will be managed on a single website, codenamed
“librement”. Two services are currently planned:

* a library service oriented around documentation that users can read/buy
* a donation service allowing users to donate money, tracking the amount
  of donations, giving public stats about it, etc.

There should be some administrative services on which the user-oriented
services can rely:

* accounting (with a double entry accounting logic)

  * each user has an account

    * record earnings of free software authors
    * records spendings of users

  * generic accounts for Freexian's own accounting (bank, receipt, paypal
    charges, etc.)

* shopping cart with payment confirmation

Generic requirements
--------------------

* The code should be documented (docstrings, using sphinx conventions).
* The website must run on a Debian Wheezy machine. You can thus assume
  Python 2.7 and Django 1.4.
