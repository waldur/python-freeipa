python-freeipa is lightweight FreeIPA client.

Features
========

- Login to FreeIPA server using username and password.
- Search for users.
- Display information about a user.
- Add, modify and delete a user.
- Get lockout status of a user account.
- Enable and disable a user account.
- Search for groups.
- Display information about a named group.
- Add, modify and delete a group.
- Add members to a group.
- Remove members from a group.
- Change user password.

Dependencies
============

The only dependency is Python Requests library (http://docs.python-requests.org/)

See also API documentation: https://ipa.demo1.freeipa.org/ipa/ui/#/p/apibrowser/

Installation
============

Install python-freeipa in development mode along with dependencies:

  .. code-block:: bash

    pip install -e .[tests]

Run tests suite:

  .. code-block:: bash

    python setup.py test


Example usage
=============

.. code-block:: python

    from python_freeipa import Client
    client = Client('ipa.demo1.freeipa.org', version='2.215')
    client.login('admin', 'Secret123')
    user = client.user_add('test3', 'John', 'Doe', 'John Doe', preferred_language='EN')
    print user
