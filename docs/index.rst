.. ceeder documentation master file, created by
   sphinx-quickstart on Fri Aug  7 14:35:10 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Ceeder: a framework for CDRs and analytics
===========================================

Release v\ |version|. (:ref:`Installation <install>`)

**ceeder** is a library that makes working with CDRs and analytics easier.

**Example code (validation)**::

  >>> from seeder import cdr
  >>> cdr()
  {'uri': 'https://qntfy.com',...
  >>> from seeder import validate
  >>> validate(cdr())
  >>> validate({"hello": "world"})
  Traceback (most recent call last):
      ...
  jsonschema.exceptions.ValidationError: 'uri' is a required property

  Failed validating 'required' in schema:
      ...
  On instance:
    {'hello': 'world'}


User guide
-------------------

.. toctree::
   :maxdepth: 2

   install
   basics
