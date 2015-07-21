django-makemessages-xgettext - Generate translations with additional options
============================================================================

:Authors:
  Resulto Developpement Web Inc.
:Version: 0.1

This project has one goal:

1. Allow makemessages to receive additional parameters to pass to xgettext.

Requirements
------------

django-makemessages-xgettext works with Python 2.7 and 3.4. It requires Django 1.7+

Installation
------------

Install with pip

::

    pip install django-makemessages-xgettext

Then add "django_makemessages_xgettext" to the INSTALLED_APPS list in settings.py

::

    INSTALLED_APPS = [
        ...
        "django_makemessages_xgettext",
    ]

Usage
-----

As a way to generate .po files without the line number comment reference
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Just use the `makemessagesxgettext` command instead of the `makemessages` command:

::

    python manage.py makemessagesxgettext -a --xgettext=--add-location=file

License
-------

This software is licensed under the `New BSD License`. See the `LICENSE` file
in the repository for the full license text.
