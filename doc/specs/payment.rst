.. _spec-payment-service:

Payment service
===============

The payment service can be used from other services to easily include
a payment button. This service should also constitute an abstraction layer
from the payment gateway.

The parts of that service that are not tightly coupled to Librement
should be bundled in a "django-payment-buttons" module and should
be hosted in a dedicated git repository under a permissive license.

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
* button text (alt attribute if image is used)
* various URL where the user can be redirected:

  * back to shop URL
  * payment accepted URL
  * payment declined URL

The payment service should send "payment_processed", "payment_accepted",
"payment_declined", "payment_pending" signals when the payment gateway sends the
server-to-server confirmation and should include all the information that
were initially submitted to create the payment button.

This allows other services to execute specific actions in response to the
payment confirmation.

All the payment information sent back by the payment gateway must be logged in
a dedicated table.

Paypal implementation
---------------------

The paypal implementation of the payment button requires to define the
paypal account to be credited in the ``paypal_email`` setting as part of
the payment options.

It should use the `PayPal Payments Standard
<https://cms.paypal.com/us/cgi-bin/?cmd=_render-content&content_ID=developer/howto_html_wp_standard_overview>`_
API together with the `Instant Payment Notification
<https://cms.paypal.com/us/cgi-bin/?cmd=_render-content&content_ID=developer/e_howto_admin_IPNIntro>`_
API to get real-time notifications of payment, refunds, etc.

It needs only support “Buy now” and “Subscribe” buttons.

CM-CIC paiement implementation
------------------------------

`CM-CIC paiement <https://www.cmcicpaiement.fr>`_ is a French payment gateway
available to customers of the Crédit Mutuel and CIC banks.

English documentation is available on request. French documentation is
available at
https://www.cmcicpaiement.fr/fr/installation/telechargements/index.html

The “Express Payment” option will be used. It allows to remember the
user's credit card number on the payment gateway associated to an “alias”.
If the customer already paid once, then he won't have to fill its credit
card number. Instead he must only fill the CVV number (3 digit number on
the back of the card).

The “Fraud prevention” option will also be activated which also provides
some supplementary parameters in the return interface.

Librement implementation
------------------------

This payment button is specific to librement and should thus be part of
the librement namespace (and not of django-payment-buttons).

The Librement implementation of the payment button allows the user to pay
with the money available on his Librement account. If the account doesn't
have enough money, then the user is transparently redirected to
Librement's default payment gateway to credit the required amount of
money.

The button can work in two modes:

* embedded: in this mode, if the user is not yet known from Librement,
  then the workflow is optimized to go directly to Librement's default
  payment gateway
* non-embedded: in this mode, if the user is not yet known from Librement,
  then the workflow offers an opportunity to login and/or to create a
  Librement account before paying.

In both modes, if the user is known from Librement, then the user is
presented with a choice of payment methods:

* (if applicable) pay everything with the Librement account
* pay everything with credit card or paypal
* (if applicable) pay €30 with Librement and the remaining with credit card or paypal

If the only applicable payment method is credit card/paypal, then the
choice screen is skipped and he's redirected straight to the
payment gateway. If the user selects a method where he pays with his
Librement account, then the form must be auto-extended with login and
password fields that must be filled to reconfirm his identity.
