# This file contains the WSGI configuration required to serve up your
# web application at http://topkek.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# Below are templates for Django and Flask.  You should update the file
# appropriately for the web framework you're using, and then
# click the 'Reload /yourdomain.com/' button on the 'Web' tab to make your site
# live.

# +++++++++++ VIRTUALENV +++++++++++
# If you want to use a virtualenv, set its path on the web app setup tab.
# Then come back here and import your application object as per the
# instructions below




# +++++++++++ FLASK +++++++++++
# Flask works like any other wsgi-compatible framework, we just need
# to import the application.  Often flask apps are called "app" so we
# may need to rename it during the import:

import os
import sys

path = '/home/topkek/gachimuchi_soundboard'
if path not in sys.path:
    sys.path.append(path)

from soundboard import app as application

# NB -- many Flask guides suggest you use a file called run.py; that's
# not necessary on PythonAnywhere.  And you should make sure your code
# does *not* invoke the flask development server with app.run(), as it
# will prevent your wsgi file from working.



# +++++++++++ GENERAL DEBUGGING TIPS +++++++++++
# getting imports and sys.path right can be fiddly!
# We've tried to collect some general tips here:
# https://www.pythonanywhere.com/wiki/DebuggingImportError



