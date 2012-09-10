.. _spec-bookstore:

The library/bookstore service
=============================

Users should be able to publish books/documentation and sell them. Other
users should be able to buy them.

Data model
----------

This probably needs refinement over time... it's thus important to be
ready to handle schema upgrades (most likely with python-django-south).

* Book (logical entity)

  * Title
  * Current BookRelease
  * slug

* BookRelease (a given version of the book)

  * Release Number
  * Title
  * Authors
  * Description
  * Sharing of benefits between multiple users (and even free software
    projects)
  * Obsolete (boolean)
  * slug

* BookProduct (a real “product” based on a BookRelease)

  * Description
  * Price
  * PricingScheme
  * ProductType (ebook/paper/both)
  * Associated files for download/online browsing
  * Enabled (allows to enable/disable a book offer)
  * Watermark (boolean, indicates whether the downloaded files must be
    watermarked with the personal info of the user)

* File (files associated to a given book release)

  * book_release_id
  * Description
  * Type (main file / additionnal file / cover / extract / table of contents)
  * Path (of the uploaded file)
  * ExtractedPath (useful only for the HTML version uploaded as an archive but
    extracted somewhere for easy access)
  * Format (PDF, EPUB, MOBI, HTML, PNG, etc.)

* BookFiles (files available for download for a given BookProduct)

  * book_product_id
  * file_id

* UserLibrary

  * user_id
  * book_product_id

Sales pages
-----------

Each book release must have a dedicated page ``/book/<slug>/`` presenting the
book and allowing the user to pick among the possible offers related to
it.

Basic features of the sales pages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Display the book cover
* Display the book price (multiple offers possible)
* Display the book authors
* Display the book description
* Provides extracts to download (table of contents, samples)
* Add to cart button

Pricing schemes
^^^^^^^^^^^^^^^

The book author can select a specific pricing scheme for each BookProduct
that he makes. Only the most basic schemes are to be implemented at the
start but later on more elaborated pricing schemes should be made
available.

Fixed net price
"""""""""""""""

The price is set once for all by the author and it includes VAT. For
example, if the price has been set to 10 EUR, a customer liable to VAT 7%
will see a gross price of 9,3 EUR and 0,7 EUR of VAT. A customer not
liable to VAT will see a gross price of 10 EUR and no VAT.

Fixed gross price
"""""""""""""""""
The price is set once for all by the author and it doesn't include VAT.
For example, if the price has been set to 10 EUR, a customer liable to VAT
7% will see a gross price of 10 EUR and 0,7 EUR of VAT. A customer not
liable to VAT will see a net price of 10 EUR and no VAT.

Minimal net price
"""""""""""""""""
It works exactly like “fixed net price” except that the user can set his
price provided that it's above the defined minimum. The amount above the
minimal price should be tracked separately from an accounting point of
view. It can use a different VAT rate and it should be possible to
“reaffect” it to somethinge else (a fundraising campaign for example).

Minimal gross price
"""""""""""""""""""
It works exactly like “fixed gross price” except that the user can set his
price provided that it's above the defined minimum. The amount above the
minimal price should be tracked separately from an accounting point of
view. It can use a different VAT rate and it should be possible to
“reaffect” it to somethinge else (a fundraising campaign for example).

Free access
"""""""""""
This pricing scheme is special. It should not appear among the available
offers. Instead it corresponds to a book product that is freely available
without registration and without adding it to one's bookshelf.

The library
-----------

The library is a file mediation service. It provides the required URLs to
access files associated to books.

Basic features of the personal bookshelf
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Display the user's collection of books
  * Display promimently books recently acquired
* Hide some books / display hidden books (useful to get read books out of
  the view)

Advanced features of the personal bookshelf
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Show when books have been updated (new BookRelease available).

