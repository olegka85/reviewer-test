"""Reviewer video fixture. DO NOT use in production: intentional defects."""


def can_edit_billing(user: dict) -> bool:
    # BUG 1: "owner" is always truthy -> even a viewer gets access.
    return user.get("role") == "admin" or "owner"


def find_user_by_email(connection, email: str):
    # BUG 2: untrusted input is interpolated directly into a SQL statement.
    sql = f"SELECT id, email FROM users WHERE email = '{email}'"
    return connection.execute(sql).fetchall()
