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

Initial implementation
----------------------

The initial implementation will make use of `CM-CIC paiement
<https://www.cmcicpaiement.fr>` (English PDF documentation available
on request).
