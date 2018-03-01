Development
===========
.. image:: https://img.shields.io/github/issues/fsi-tue/fachschaftsempfaenger.svg
    :target: https://github.com/fsi-tue/fachschaftsempfaenger/issues

.. image:: https://img.shields.io/github/issues-pr/fsi-tue/fachschaftsempfaenger.svg
    :target: https://github.com/fsi-tue/fachschaftsempfaenger/pulls


Getting Involved
----------------

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


Adapt it to your own needs
--------------------------

The following workflow also works fine if you are interested in creating your
own infoscreen. Except submitting Pull Requests to our own repository, simply
reimplement the submodules and views to your own needs.


Workflow
--------

1. Fork this repository on Github. From here on we assume you successfully
   forked this repository to
   https://github.com/yourname/fachschaftsempfaenger.git

2. Install *fachschaftsempfaenger* locally in development mode

.. code:: bash

    git clone https://github.com/yourname/fachschaftsempfaenger.git
    cd fachschaftsempfaenger
    python setup.py develop --user

3. Install a django development server on your machine with

.. code:: bash

    django-admin startproject your-project

4. Add *fachschaftsempfaenger* to your ``INSTALLED_APPS`` in
   ``your-project/mysite/settings.py``:

.. code-block:: python

   INSTALLED_APPS = [
       ...,
       'fachschaftsempfaenger'
   ]

5. Add code, tests or documentation.

.. note::

    If you are from another student union we recommend to reimplement all
    submodules to your own needs.

6. Add and commit your changes.

   .. code:: bash

       git add -u
       git commit -m 'fixes #42 by posing the question in the right way'

   You can reference relevant issues in commit messages (like #42) to make GitHub
   link issues and commits together, and with phrase like "fixes #42" you can
   even close relevant issues automatically.

7. Push your local changes to your fork:

  .. code:: bash

      git push git@github.com:yourname/fachschaftsempfaenger.git

8. If the changes you made are relevant for our project, feel free to submit a
   Pull Request at https://github.com/yourname/fachschaftsempfaenger/pulls and
   click "New pull request" to submit your Pull Request to
   https://github.com/fsi-tue/fachschaftsempfaenger.


Building documentation
----------------------

The projects documentation is stored in the ``doc/`` folder and is created with
``sphinx``. You can rebuild the documentation by executing

.. code:: bash

   make html

in the documentation folder.
