   **********   Django Static files tutorial *********
1. Edit settings.py for database settings
2. Place the static files "files1.txt", "files2.txt" in the directory for example "/home/notroot/django_tut/staticfiles/sfiles"
3. create the directory files in the path for example "/home/notroot/django_tut/staticfiles/"
4. edit section  STATICFILES_DIRS in settings.py file with the value
"/home/notroot/django_tut/staticfiles/sfiles"
5. edit section in STATIC_ROOT in settings.py file with the value "/home/notroot/django_tut/staticfiles/files"
6. set the value for the variable in settings.py STATIC_URL = '/static/'
7. write a template in the template dir for example index.html
{% load staticfiles %}
  <a href="{% static 'files1.txt' %}">link1</a>
  <a href="{% static 'files2.txt' %}">link2</a>
8. update the TEMPLATE_DIRS option in the settings.py.
9. Add a view in the views.py and update urls.py file
10. In the project root folder run the command "python manage.py collectstatic"
out put would be

You have requested to collect static files at the destination
location as specified in your settings.

This will overwrite existing files!
Are you sure you want to do this?

Type 'yes' to continue, or 'no' to cancel: yes

0 static files copied, 73 unmodified.
11. access the url from the browser

http://127.0.0.1:8000/staticfiles/
  

Note: This is compatible with django 1.5.4
