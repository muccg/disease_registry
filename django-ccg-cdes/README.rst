=====
ccg-cdes
=====
ccg-cdes provides models for Common Data Elements

Quick start
-----------

1. Add "cdes" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'ccg-cdes',
      )

2. Include the cdes URLconf in your project urls.py like this::

      url(r'^cdes/', include('ccg-cdes.urls')),

3. Run `python manage.py migrate` to create the ccg-cdes models.

