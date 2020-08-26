![image][]

[![image][1]][2]

[![image][3]][4]

[![Documentation Status][]][5]

*Fachschaftsempfaenger* is a Django application created by the [student union of Computer Science][] at the university of Tuebingen to provide a simple screen with important information for the students and employees at department of Computer Science in Tuebingen.

Installation with pip
=====================

Checkout the pip branch more information.

Installation with docker
========================

This is for testing and local deployment purposes. For instances facing the internet or production mode, see this [config][].

Install docker and docker-compose on your system (with your package manager or manually).

Clone this repo (or use the HTTPS variant):

```git clone git@github.com:fsi-tue/fachschaftsempfaenger.git```


Build the image and start the container with docker-compose (--build is only needed for the first time or when changing things in requirements.txt):

```sudo docker-compose up -d --build```


Also execute the script (you also need to do this when upgrading Django etc.):

```sudo docker-compose exec web bash /code/script.sh```


When finished, remove the container:

```sudo docker-compose down```

Documentation
=============

*fachschaftsempfaenger* uses `sphinx` to create a documentation manual.
The documentation can be found [here][5].

Getting involved
================

The *fachschaftsempfaenger* project welcomes help in the following ways:

-   Making Pull Requests for [code][], or [documentation][].
-   Commenting on [open issues][] and [pull requests][].
-   Helping to answer [questions in the issue section][].
-   Creating feature requests or adding bug reports in the [issue
    section][].

For more information on how to contribute to *fachschaftsempfaenger* have a look at the [development section][].

  [image]: docs/source/_static/img/logo.png
  [1]: https://img.shields.io/github/license/fsi-tue/fachschaftsempfaenger.svg
  [2]: https://github.com/fsi-tue/fachschaftsempfaenger/blob/master/LICENSE.txt
  [3]: https://pyup.io/repos/github/fsi-tue/fachschaftsempfaenger/shield.svg
  [4]: https://pyup.io/repos/github/fsi-tue/fachschaftsempfaenger/
  [Documentation Status]: https://readthedocs.org/projects/fachschaftsempfaenger/badge/?version=latest
  [5]: https://fachschaftsempfaenger.readthedocs.io/en/latest/index.html
  [student union of Computer Science]: http://www.fsi.uni-tuebingen.de/
  [config]: https://github.com/fsi-tue/docker/tree/master/fachschaftsempfaenger
  [code]: https://github.com/fsi-tue/fachschaftsempfaenger/tree/master/fachschaftsempfaenger
  [documentation]: https://github.com/fsi-tue/fachschaftsempfaenger/tree/master/doc
  [open issues]: https://github.com/fsi-tue/fachschaftsempfaenger/issues
  [pull requests]: https://github.com/fsi-tue/fachschaftsempfaenger/pulls
  [questions in the issue section]: https://github.com/fsi-tue/fachschaftsempfaenger/labels/question
  [issue section]: https://github.com/fsi-tue/fachschaftsempfaenger/issues/new
  [development section]: https://fachschaftsempfaenger.readthedocs.io/en/latest/development.html
