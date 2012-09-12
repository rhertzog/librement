.. _spec-payment-service:

Payment service
===============

The payment service can be used from other services to easily include
a payment button. This service should also constitute an abstraction layer
from the payment gateway.

Design
------

A custom django template tag representing the payment button seems
appropriate. It would take a configuration object as parameter defining
its appearance and its behaviour:

* order date
* order reference
* user email
* language
* buying options (a list is only shown if multiple options are listed)

  * short description (embedded in a drop-down list)
  * amount
  * currency
  * recurrence (subscription with payment every X months)
  * a set of custom fields (required to identify the product bought and
    validate its price)

* payment options
* button image URL
* various URL where the user can be redirected:

  * back to shop URL
  * payment accepted URL
  * payment declined URL

The payment service should send "payment_processed", "payment_accepted",
"payment_declined" signals when the payment gateway sends the
server-to-server confirmation and should include all the information that
were initially submitted to create the payment button.

This allows other services to execute specific actions in response to the
payment confirmation.

All the payment information sent back by the payment gateway must be logged in
a dedicated table.

Initial implementation
----------------------

The initial implementation will make use of `CM-CIC paiement
<https://www.cmcicpaiement.fr>`_ (English PDF documentation available
on request).

The “Express Payment” option will be used. It allows to remember the
user's credit card number on the payment gateway associated to an “alias”.
If the customer already paid once, then he won't have to fill its credit
card number. Instead he must only fill the CVV number (3 digit number on
the back of the card).

The payment form can thus accept supplementary parameters which
are not documented in the English PDF documentation:

=============  ==========================================  =================
Option         Description                                 Example
=============  ==========================================  =================
aliascb        Alias of a customer's credit card.          aliascb=customer1
               Format: [a-zA-Z0-9]{1,64}
forcesaisiecb  Can be used to force the customer to input  forcesaisiecb=1
               the full credit card number even though
               he already paid once under the given
               alias.
=============  ==========================================  =================

And the return interface also receives supplementary parameters:

=============  ==========================================  =================
Option         Description                                 Example
=============  ==========================================  =================
cbenregistree  Boolean indicating whether the card has     cbenregistree=1
               been recorded under a given "aliascb".
               1: yes
               0: no
cbmasquee      6 first and 4 last digits of the            cbmasquee=123456******7890
               customer's credit card, separated by
               stars. Available only when
               cbenregistree=1.
=============  ==========================================  =================

The “Fraud prevention” option will also be activated which also provides
some supplementary parameters in the return interface.

