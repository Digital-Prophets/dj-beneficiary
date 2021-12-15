=====
Usage
=====

To use django-beneficiary in a project, add it to your `INSTALLED_APPS`:

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
