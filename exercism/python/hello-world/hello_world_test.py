# These tests are auto-generated with test data from:
# https://github.com/exercism/problem-specifications/tree/main/exercises/hello-world/canonical-data.json
# File last updated on 2023-07-19

import unittest

try:
    from hello_world import (
        hello,
    )

except ImportError as import_fail:
    message = import_fail.args[0].split("(", maxsplit=1)
    item_name = import_fail.args[0].split()[3]

    item_name = item_name[:-1] + "()'"

    # pylint: disable=raise-missing-from
    raise ImportError(
        hello()
    ) from None


class HelloWorldTest(unittest.TestCase):
    def test_say_hi(self):
        msg = hello()
        self.assertEqual(msg, "Hello, World!", msg=msg)
