Genealogy Data Models
=====================

*GDM* is a set of simple Django models for genealogy based data
structures (family trees).

Quick start
-----------

1. Add "gdm" to your INSTALLED\_APPS setting like this:

   .. code:: python

       INSTALLED_APPS = (
           ...
           'gdm',
       )

2. Run ``python manage.py migrate`` to create the GDM models.

3. Include the GDM models in your project like this:

   .. code:: python

       from gdm.models.tree import Person, Family

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create persons and families (you'll need the Admin app enabled).
