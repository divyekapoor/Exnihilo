Adobe Ex-Nihilo
===============

This site was built for a contest conducted as a part of Cognizance 2011. 

This site is the contest site for a fictitious company Lebensraum worth $50 billion.
The site is meant to promote its new SUV - Meister.

The actual problem statement required the use of HTML5 and CSS3 media queries. 

See: ExNihiloStage.pdf for the problem statement.

Usage
=====

To see how the site performs:

Install Python Prerequisites 

    sudo apt-get install python-django
    sudo easy_install djangoratings
    sudo easy_install simplejson

Install Server Side Javascript Prerequisites

    sudo apt-get install nodejs (or alternatively, get node.js from github and follow the instructions)
    Install `npm` from http://github.com/isaacs/npm
    sudo npm install node-static

Install yui-compressor to minimize CSS and JS

    sudo apt-get install yui-compressor

Install sqlite3 (if not present)

    sudo apt-get install sqlite3

Create a local database copy

    cd exnihilo
    ./manage.py syncdb
    cd ..

Run the development server

    make runserver

View the site at http://localhost:8000/

Note: a sample httpd.conf and exnihilo/apache/django.wsgi is supplied for production mode.



Listing of Tech Used for the Contest
===================================

Adobe Photoshop
Adobe Illustrator
Adobe After Effects CS4
Adobe Dreamweaver CS5 (media query and multiscreen preview features)

AJAX
YUI-reset
YUI-compressor
node.js
less.js
node-static
jquery and libraries
CSS3
HTML5
python
WSGI
django
make
gcc
git
