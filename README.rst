=======================
Potato Simple Blog Demo
=======================

This is a simple blogging application built using Google App Engine and
Django. It doesn't do much - not much at all!

The app is up an running at http://potatodemo.appspot.com/ with the admin
accessible at http://potatodemo.appspot.com/admin. You can log in to the admin
using the following details::

  username: potato
  password: potato

Features
========

- Create, read, update and delete blog entries using the Django admin
- Basic HTML frontend
- Write blog entries using RestructuredText

Notes
=====

Since this is my first time using App Engine in any way, I've concentrated on
trying to get an app up and running that is reasonably complete and usable as
opposed to pretty and feature rich.

Ordinarily I would include a setup.py file to create packages which
are installable using setuptools. I have skipped this step for now, since GAE
has its own means of deploying apps (eg. using `appcfg.py update`).

I've included some unit tests inside blog/tests.py - simple view tests as well
as a few tests I wrote during development to explore the consequences of
running Django with the GAE Datastore. As expected, the Datastore is not able
to provide `uniqueness guarantees`_ across Entities making it harder to work
with, say, usernames, emails or slugs which need to be unique. Having worked
with CouchDB in the past, I know that it is possible to store unique values
as part of the unique key for an entry which the database can ensure is unique
- perhaps a similar workaround would be possible on App Engine too.

The repository is not complete - I've .gitignored the django apps the project
depends on (dbindexer, djangononrel, djangoappengine, djangotoolbox, docutils)
to keep this repository small and easily digestible.


References & Examples Used
==========================

- Credits to Andi Albrecht for showing how to use `docutils on App Engine`_.
- This app was built using the "django-testapp" application on the
  `allbuttonspressed`_ site as a starting point.


.. _`uniqueness guarantees`: http://code.google.com/p/googleappengine/issues/detail?id=178&colspec=ID%20Type%20Status%20Priority%20Stars%20Owner%20Summary%20Log%20Component
.. _`docutils on App Engine`: http://automatictaxistop.blogspot.com/2008/07/using-restructuredtext-with-google-app.html
.. _`allbuttonspressed`: http://www.allbuttonspressed.com/projects/djangoappengine