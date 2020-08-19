.. _basics:

Basic usage of Ceeder
========================


This part of the documentation covers the basic usage of ceeder.


CDRs and validation
-----------------------------

Use the `cdr()` function to obtain an example CDR dictionary.
Use the `validate(dict)` function to validate a CDR-like dict.
`validate` throws an exception if any issues are found,
such as a missing required field.

  >>> from seeder import cdr, validate
  >>> validate(cdr())
  >>> validate({"hello": "world"}
  Traceback (most recent call last):
      ...
  jsonschema.exceptions.ValidationError: 'uri' is a required property

  Failed validating 'required' in schema:
      ...
  On instance:
    {'hello': 'world'}


This could be wrapped in a `try` block for more resilient error
handling.
