# Genealogy Data Models
[![django-gdm-dm](https://img.shields.io/pypi/dm/django-gdm.svg)](https://pypi.python.org/pypi/django-gdm/)
[![django-gdm-v](https://img.shields.io/pypi/v/django-gdm.svg)](https://pypi.python.org/pypi/django-gdm/)
[![django-gdm-bl](https://img.shields.io/badge/license-MIT-blue.svg)](https://pypi.python.org/pypi/django-gdm/)

_GDM_ is a set of simple Django models for genealogy based data
structures (family trees).

## Quick start
1. Add "gdm" to your INSTALLED_APPS setting like this:

    ```python
    INSTALLED_APPS = (
        ...
        'gdm',
    )
    ```

2. Run `python manage.py migrate` to create the GDM models.

3. Include the GDM models in your project like this:

    ```python
    from gdm.models.tree import Person, Family
    ```

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create persons and families (you'll need the Admin app enabled).
