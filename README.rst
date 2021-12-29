=============================
django-beneficiary
=============================

.. image:: https://badge.fury.io/py/dj-beneficiary.svg
    :target: https://badge.fury.io/py/dj-beneficiary

.. image:: https://travis-ci.org/sonlinux/dj-beneficiary.svg?branch=master
    :target: https://travis-ci.org/sonlinux/dj-beneficiary

.. image:: https://codecov.io/gh/sonlinux/dj-beneficiary/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/sonlinux/dj-beneficiary

A beneficiary in either a health facility or in project implementation.

Documentation
-------------

The full documentation is at https://dj-beneficiary.readthedocs.io.

Quickstart
----------

Install django-beneficiary::

    pip install dj-beneficiary

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dj_beneficiary.apps.DjBeneficiaryConfig',
        ...
    )

Add django-beneficiary's URL patterns:

.. code-block:: python

    from dj_beneficiary import urls as dj_beneficiary_urls


    urlpatterns = [
        ...
        url(r'^', include(dj_beneficiary_urls)),
        ...
    ]

Features
--------

* TODO

Running in Development
----------------------

Are you writing code to improve this package?

::

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    pip install -r requirements_dev.txt
    
    # then you can work with regular django development commands
    python manage.py migrate
    python manage.py collectstatic
    python manage.py createsuperuser
    python manage.py runserver

    # and happy coding!

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

`Digital Prophets <https://digiprophets.com>`__
