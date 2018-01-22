Administration
==============
The content of some tiles can be changed via the Django admin. Once a user with
``staff`` privileges is created, the Django admin can be accessed under ``/admin``.

Advertisements
--------------
An advertisement consists of an image and an optional text. This way, one can
put images of flyers, posters etc. into this tile to advertise for events
of the local student union. Each ad has a start and end date to mark the duration
in which the ad should be displayed.

.. image:: _static/img/ad_admin.png

Once you upload a number of ad images, one will be chosen at random each time
the tile is reloaded. This behaviour can be changed by adjusting the *QuerySet*
inside the ``advertisement_tile`` view inside ``views.py``:


.. code-block:: python

  qs = Advertisement.objects.filter(start_date__gte=timezone.now()).order_by('?').first()
