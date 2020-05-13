# django-sympycharfield
Django Char Field using Sympy

## Desciption
SympyCharField is a simple Django app to use Sympy through a CharField.

Detailed documentation is in the "docs" directory.

## Install
Run the command in the terminal::

    pip install django-sympycharfield

## Quick start
1. Import in your models.py::

    from sympycharfield.models import SympyCharField

2. Use it as CharField.

## Test
1. If you would like to check if SympyCharField is working fine, add
"SympyCharField" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'sympycharfield',
    ]

2. Include the SympyCharField URLconf in your project urls.py like this::

    path('sympycharfield/', include('sympycharfield.urls')),

3. Run `python manage.py makemigrations sympycharfield` to create the sympycharfield models.

4. Run `python manage.py migrate` to create the sympycharfield models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a sympycharfield (you'll need the Admin app enabled).

6. Visit http://127.0.0.1:8000/sympycharfield/ to check.