Installation
============

This repository contains a fully functional version of *fachschaftsempfaenger*
as it is run by the student union of Computer Science at the university of
Tuebingen. This guide aims to instruct you to get your version runnung either in
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
      mysite/
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

4. Make the migrations to adapt the database scheme locally:

.. code-block:: bash

    python manage.py migrate
    python manage.py makemigrations fachschaftsempfaenger
    python manage.py migrate fachschaftsempfaenger


5. Define a superuser to access the Django admin:

.. code-block:: bash

    python manage.py createsuperuser


6. Start a local server:

.. code-block:: bash

    python manage.py runserver

7. Open a browser and go to http://127.0.0.1:8000/


Production Server
-----------------

.. note::

    This section is still under construction.
