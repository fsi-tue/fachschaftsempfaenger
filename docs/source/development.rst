Development
===========
.. image:: https://img.shields.io/github/issues/fsi-tue/fachschaftsempfaenger.svg
    :target: https://github.com/fsi-tue/fachschaftsempfaenger/issues

.. image:: https://img.shields.io/github/issues-pr/fsi-tue/fachschaftsempfaenger.svg
    :target: https://github.com/fsi-tue/fachschaftsempfaenger/pulls


Getting Involved
----------------

The *Fachschaftsempfaenger* project welcomes help in the following ways:

    * Making Pull Requests for
      `code <https://github.com/fsi-tue/fachschaftsempfaenger/tree/master/fachschaftsempfaenger>`_,
      or `documentation <https://github.com/fsi-tue/fachschaftsempfaenger/tree/master/doc>`_.
    * Commenting on `open issues <https://github.com/fsi-tue/fachschaftsempfaenger/issues>`_
      and `pull requests <https://github.com/fsi-tue/fachschaftsempfaenger/pulls>`_.
    * Helping to answer `questions in the issue section
      <https://github.com/fsi-tue/fachschaftsempfaenger/labels/question>`_.
    * Creating feature requests or adding bug reports in the `issue section
      <https://github.com/fsi-tue/fachschaftsempfaenger/issues/new>`_.


Workflow
--------

1. Fork this repository on Github. From here on we assume you successfully
   forked this repository to
   https://github.com/yourname/fachschaftsempfaenger.git

2. Get a local copy of your fork and run the Django server locally.

.. code:: bash

    git clone https://github.com/yourname/fachschaftsempfaenger.git
    cd fachschaftsempfaenger
    python3 manage.py runserver

3. Add code, tests or documentation. You can reference relevant issues in
   commit messages (like #42) to make GitHub link issues and commits together,
   and with phrase like "fixes #42" you can even close relevant issues
   automatically.

4. Push your local changes to your fork:

.. code:: bash

    git push git@github.com:yourname/fachschaftsempfaenger.git

5. Open the Pull Requests page at
   https://github.com/yourname/fachschaftsempfaenger/pulls and
   click "New pull request" to submit your Pull Request to
   https://github.com/fsi-tue/fachschaftsempfaenger.


Building documentation
----------------------

The projects documentation is stored in the ``doc/`` folder and is created with
``sphinx``. You can rebuild the documentation by executing

.. code:: bash

   make html

in the documentation folder.
