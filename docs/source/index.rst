Welcome to FreeIPA client's documentation!
===========================================

Example usage
-----------------------------

.. code-block:: python

    from python_freeipa import Client
    client = Client('ipa.demo1.freeipa.org', version='2.215')
    client.login('admin', 'Secret123')
    user = client.user_add('test3', 'John', 'Doe', 'John Doe', preferred_language='EN')
    print user

python\_freeipa.client module
-----------------------------

.. automodule:: python_freeipa.client
    :members:
    :undoc-members:
    :show-inheritance:

python\_freeipa.exceptions module
---------------------------------

.. automodule:: python_freeipa.exceptions
    :members:
