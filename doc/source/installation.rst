#########################################
CloudKitty installation and configuration
#########################################


Install from source
===================

There is no release of CloudKitty as of now, the installation can be done from
the git repository.

Retrieve and install CloudKitty :

::

    git clone git://git.openstack.org/stackforge/cloudkitty
    cd cloudkitty
    python setup.py install

This procedure installs the ``cloudkitty`` python library and a few
executables:

* ``cloudkitty-api``: API service
* ``cloudkitty-processor``: Processing service (collecting and rating)
* ``cloudkitty-dbsync``: Tool to create and upgrade the database schema
* ``cloudkitty-storage-init``: Tool to initiate the storage backend
* ``cloudkitty-writer``: Reporting tool

Install a sample configuration file :

::

    mkdir /etc/cloudkitty
    cp etc/cloudkitty/cloudkitty.conf.sample /etc/cloudkitty/cloudkitty.conf

Configure CloudKitty
====================

Edit :file:`/etc/cloudkitty/cloudkitty.conf` to configure CloudKitty.

The following shows the basic configuration items:

.. code-block:: ini

    [DEFAULT]
    verbose = True
    log_dir = /var/log/cloudkitty

    rabbit_host = RABBIT_HOST
    rabbit_userid = openstack
    rabbit_password = RABBIT_PASSWORD

    [auth]
    username = cloudkitty
    password = CK_PASSWORD
    tenant = service
    region = RegionOne
    url = http://localhost:5000/v2.0

    [database]
    connection = mysql://cloudkitty:CK_DBPASS@localhost/cloudkitty

    [ceilometer_collector]
    username = cloudkitty
    password = CK_PASSWORD
    tenant = service
    region = RegionOne
    url = http://localhost:5000

Setup the database and storage backend
======================================

MySQL/MariaDB is the recommended database engine. To setup the database, use
the ``mysql`` client:

::

    mysql -uroot -p << EOF
    CREATE DATABASE cloudkitty;
    GRANT ALL PRIVILEGES ON cloudkitty.* TO 'cloudkitty'@'localhost' IDENTIFIED BY 'CK_DBPASS';
    EOF

Run the database synchronisation scripts:

::

    cloudkitty-dbsync upgrade

Init the storage backend:

::

    cloudkitty-storage-init

Setup Keystone
==============

CloudKitty uses Keystone for authentication, and provides a ``rating`` service.

To integrate CloudKitty to Keystone, run the following commands (as OpenStack
administrator):

::

    keystone user-create --name cloudkitty --pass CK_PASS
    keystone user-role-add --user cloudkitty --role admin --tenant service

Give the ``rating`` role to ``cloudkitty`` for each tenant that should be
handled by CloudKitty:

::

    keystone role-create --name rating
    keystone user-role-add --user cloudkitty --role rating --tenant XXX

Create the ``rating`` service and its endpoints:

::

    keystone service-create --name CloudKitty --type rating
    keystone endpoint-create --service-id RATING_SERVICE_ID \
        --publicurl http://localhost:8888 \
        --adminurl http://localhost:8888 \
        --internalurl http://localhost:8888

Start CloudKitty
================

Start the API and processing services :

::

    cloudkitty-api --config-file /etc/cloudkitty/cloudkitty.conf
    cloudkitty-processor --config-file /etc/cloudkitty/cloudkitty.conf