Account management and public profiles
======================================

.. _spec-std-account:

Standard account management
---------------------------

#. Users can create an account with email + password (confirmation by email
   required).

   #. Required fields: country / first name / last name
   #. Optional field: address / zip-code / city / state / phone

#. Users can attach multiple (confirmed) email addresses to a single
   account.
#. Users can login with an email + their password.
#. Users can recover a lost password (by giving their email).

Advanced account management
---------------------------

.. note:: To be specified.

.. _spec-basic-profile:

Basic public profile
--------------------

Users should be able to activate a public profile where they can fill all
those fields:

1. Display name (only required field, defaults to first + last name)
2. Unique account name (slug to be used in URLs, derived from display name
   by default with accented characters dropped and spaces replaced by a
   dash)
3. Picture
4. Bio
5. Multiple URLs (Website, Blog, Social accounts, etc.)

The public profile should be visible from ``/people/<user-slug>/``.

Advanced public profile
-----------------------

.. note:: To be specified.
