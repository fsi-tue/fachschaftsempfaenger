
.. image:: docs/source/_static/img/logo.png

.. image:: https://img.shields.io/github/license/fsi-tue/fachschaftsempfaenger.svg
    :target: https://github.com/fsi-tue/fachschaftsempfaenger/blob/master/LICENSE.txt

.. image:: https://pyup.io/repos/github/fsi-tue/fachschaftsempfaenger/shield.svg
    :target: https://pyup.io/repos/github/fsi-tue/fachschaftsempfaenger/

.. image:: https://readthedocs.org/projects/fachschaftsempfaenger/badge/?version=latest
    :target: https://fachschaftsempfaenger.readthedocs.io/en/latest/index.html
    :alt: Documentation Status

*Fachschaftsempfaenger* is a Django application created by the `student
union of Computer Science <http://www.fsi.uni-tuebingen.de/>`_ at the
university of Tuebingen to provide a simple screen with important information
for the students and employees at department of Computer Science in Tuebingen.

Installation with pip
=====================

Checkout the pip branch more information.


Installation with docker
========================

This is for testing and local deployment purposes. For instances facing the internet or production mode, see this `config <https://github.com/fsi-tue/docker/tree/master/fachschaftsempfaenger>`_.

Install docker and docker-compose on your system (with your package manager or manually).

Clone this repo (or use the HTTPS variant):
.. code:: bash

    git clone git@github.com:fsi-tue/fachschaftsempfaenger.git


Build the image and start the container with docker-compose (--build is only needed for the first time or when changing things in requirements.txt).
Also execute the script (you also need to do this when upgrading Django etc.):
.. code:: bash

    sudo docker-compose up -d --build
    sudo docker-compose exec web bash /code/script.sh


 When finished, remove the container:
.. code:: bash

    sudo docker-compose down


Documentation
=============

*fachschaftsempfaenger* uses ``sphinx`` to create a documentation manual.
The documentation can be found `here
<https://fachschaftsempfaenger.readthedocs.io/en/latest/index.html>`_.


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
look at the `development section
<https://fachschaftsempfaenger.readthedocs.io/en/latest/development.html>`_.


Acknowledgments
===============
*Fachschaftsempfaenger* is largely inspired by the infoscreen of the student
union of Computer Science at the university Freiburg. We are grateful for their
provided source code which helped a lot building this app.
