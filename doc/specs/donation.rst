.. _spec-donation:

The donation service
====================

Convincing people to donate is hard. But it's easier if there's
some transparency in the donation process (public list of donors)
and if there are clear goals to the donation (financial targets and
concrete use of the corresponding money). Adding a time limit also
helps to convince donors to donate now instead of postponing it to
later.

Librement's donation service make it easy to host effective donation
drives with multiple widgets that you can embed on your own website.

Within the donation service, developers can manage any number of donation
trackers. A donation tracker defines the specifics of the donation drive
(limited in time or not, financial target, whether the list of donors is
public, etc.) and contains all the details of donations and donators. It
has a unique identifier for reference purpose.

List of donation trackers
-------------------------

The main screen of the donation service lists all the active donation
trackers with the following information:

* name of the donation tracker
* type of the donation tracker (permanent, time limited)
* start datetime
* end datetime (can be unset)
* target (can be unset)
* period (only for permanent donation trackers)
* amount raised

  * in time limited campaigns: total amount raised
  * in permanent campaigns: amount raised in the current period

Clicking on the name of a donation tracker brings you to a screen
with details of the donations recorded in this tracker. The list also
contains shortcut links to the various operations that can be done
on each tracker (see further for details).

The main screen also offers a button to create a new donation tracker.

Edition / creation of a donation tracker
----------------------------------------

This page contains a big form with many parameters describing the
donation tracker:

* its name (required)
* its type (required)

  * permanent
  * time-limited

* its start datetime (defaults to now, required, can be hidden for
  permanent campaigns)
* its end datetime (default to unset, required for time limited campaigns)
* its period (day, week, month, quarter, semester, year)
  (visible and required only for permanent campaigns, unset for time
  limited campaigns)
* its currency: EUR, USD, etc. (required)
* its target: the amount of money to raise (optional)
* whether to publish the list of donors (checkbox, boolean)
* a thank you URL: a URL where the user is redirected after having
  completed a donation (optional)

Operations on donation trackers
-------------------------------

Many operations are possible on donation trackers:

* close the tracker: this is done by setting its end datetime to a date in
  the past
* add a manual donation: record a donation that happened outside of the
  donation form (because it happened in real life, or because the donor
  used a payment system not offered by Librement)
* add a thank-you email: configure a custom email to be sent back to
  donors that left their email (or where we got it through the payment
  system)
* get HTML for widgets: retrieve HTML code to embed Librement widgets
  in a website

Details of a donation tracker
-----------------------------

Hosted donation page
--------------------

HTML widgets
------------


