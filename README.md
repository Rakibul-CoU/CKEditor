This Project is to check how CKEditor can be used to customize a field of a django model.
Install ckeditor through terminal:
pip install django-ckeditor

Then include 'ckeditor' in settings.py.

You can add more customization in settings.py.

Then add a form class in forms.py under app. In this class customize which field you want to customize.

Then call the form to admin.py file under that model's admin class.
