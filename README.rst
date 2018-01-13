
.. image:: docs/source/_static/img/logo.png

.. image:: https://img.shields.io/github/license/fsi-tue/fachschaftsempfaenger.svg
    :target: https://github.com/fsi-tue/fachschaftsempfaenger/blob/master/LICENSE.txt

*Fachschaftsempfaenger* is a Django application created by the `student
union of Computer Science <http://www.fsi.uni-tuebingen.de/>`_ at the
university of Tuebingen to provide a simple screen with important information
for the students and employees at department of Computer Science in Tuebingen.

Quickstart
==========

1. Clone this repository

.. code-block:: bash

    git clone https://github.com/fsi-tue/fachschaftsempfaenger.git

2. Change directory to the cloned project and install the requirements

.. code-block:: bash

    cd fachschaftsempfaenger
    pip install -r requirements.txt

3. Make the migrations

.. code-block:: bash

    python manage.py migrate

4. Start a local server:

.. code-block:: bash

    python manage.py runserver

5. Open a browser and go to http://127.0.0.1:8000/

Documentation
=============

*fachschaftsempfaenger* uses ``sphinx`` to create a documentation manual.
The documentation can be found `here <>`_.

Getting involved
================

The *fachschaftsempfaenger* project welcomes help in the following ways:

* Making Pull Requests for
  `code <https://github.com/fsi-tue/fachschaftsempfaenger/tree/master/fachschaftsempfaenger>`_,
  or `documentation <https://github.com/fsi-tue/fachschaftsempfaenger/tree/master/doc>`_.
* Commenting on `open issues <https://github.com/fsi-tue/fachschaftsempfaenger/issues>`_
  and `pull requests <https://github.com/fsi-tue/fachschaftsempfaenger/pulls>`_.
* Helping to answer `questions in the issue section
  <https://github.com/fsi-tue/fachschaftsempfaenger/labels/question>`_.
* Creating feature requests or adding bug reports in the `issue section
  <https://github.com/fsi-tue/fachschaftsempfaenger/issues/new>`_.

For more information on how to contribute to *fachschaftsempfaenger* have a
look at the `development section <>`_.

Acknowledgments
===============
*Fachschaftsempfaenger* is largely inspired by the infoscreen of the student
union of Computer Science at the university Freiburg. We are grateful for their
provided source code which helped a lot building this app.
