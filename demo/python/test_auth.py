"""Regression tests intentionally FAIL before the security fixes."""

import sqlite3
import unittest

from auth import can_edit_billing, find_user_by_email


class ReviewerVideoTests(unittest.TestCase):
    def test_viewer_cannot_edit_billing(self):
        self.assertFalse(can_edit_billing({"role": "viewer"}))

    def test_sql_injection_does_not_bypass_filter(self):
        database = sqlite3.connect(":memory:")
        self.addCleanup(database.close)
        database.execute("CREATE TABLE users (id INTEGER, email TEXT)")
        database.executemany(
            "INSERT INTO users (id, email) VALUES (?, ?)",
            [(1, "alice@example.test"), (2, "bob@example.test")],
        )
        self.assertEqual(find_user_by_email(database, "' OR 1=1 -- "), [])


if __name__ == "__main__":
    unittest.main()
