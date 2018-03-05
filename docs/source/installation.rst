Installation
============

This repository contains a fully functional version of *fachschaftsempfaenger*
as it is run by the student union of Computer Science at the university of
Tuebingen. This guide aims to instruct you to get your version running either in
development mode on your PC or on a production version on a server.


.. note:

    If you are interested in adding a new feature for our student union or you
    want to use *fachschaftsempfaenger* for your student union as well, please
    have a look at :ref:`development`.


Development Server
------------------

1. The easiest way to use this application is to install it via ``pip``:

.. code-block:: bash

    pip install git+https://github.com/fsi-tue/fachschaftsempfaenger

*fachschaftsempfaenger* is now installed as a normal python package.

2. Install a Django Development Server on your local machine.

.. code-block:: bash

    django-admin startproject yourproject

This will create a `yourproject` directory in your current directory:

.. code-block:: bash

    yourproject/
      manage.py
      yourproject/
          __init__.py
          settings.py
          urls.py
          wsgi.py

3. Add *fachschaftsempfaenger* to your ``INSTALLED_APPS`` in ``settings.py``:

.. code-block:: python

    INSTALLED_APPS = [
        ...,
        'fachschaftsempfaenger'
    ]

4. Adjust your ``settings.py`` to accomodate uploads made by *fachschaftsempfaenger*:

.. code-block:: python

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/

    ...
    MEDIA_URL = '/uploads/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

5. Adjust ``urls.py`` to make your installation of *fachschaftsempfaenger* reachable:

.. code-block:: python

    ...
    from .settings import MEDIA_URL, MEDIA_ROOT
    from django.urls import path, re_path, include
    from django.conf.urls.static import static

    urlpatterns = [
    ...
    re_path(r'^', include('fachschaftsempfaenger.urls')),
    ...
    ] + static(MEDIA_URL, document_root=MEDIA_ROOT) # this make the uploads folder reachable

6. Make the migrations to adapt the database scheme locally:

.. code-block:: bash

    python manage.py migrate
    python manage.py makemigrations fachschaftsempfaenger
    python manage.py migrate fachschaftsempfaenger


7. Define a superuser to access the Django admin:

.. code-block:: bash

    python manage.py createsuperuser


8. Start a local server:

.. code-block:: bash

    python manage.py runserver

9. Open a browser and go to http://127.0.0.1:8000/


Production Server
-----------------

.. note::

    This section is still under construction.
