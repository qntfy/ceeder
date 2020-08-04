# seeder examples

This directory shows an extremely simple usage pattern for the `seeder`
library.

Write a function that takes in a `string` (the `extracted_text` field from the CDR)
and outputs a list of dictionaries that contain `tag`-like annotations.

That can then be passed in to the `TagAnnotator` as a parameter,
along with the label of the analytic output.

See the test file for inspiration about how to test this in your program.
