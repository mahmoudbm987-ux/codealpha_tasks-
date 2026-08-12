
# Secure Coding Review

## Project Overview

This project demonstrates a secure coding review using Python and SQLite.

Two versions of a simple login application were created:

- `vulnerable_app.py` — contains an SQL Injection vulnerability.
- `secure_app.py` — fixes the vulnerability using parameterized SQL queries.

## Vulnerability Found

### SQL Injection

The vulnerable application builds the SQL query by directly concatenating user input with the SQL statement.

This can allow malicious input to change the intended SQL query.

### Vulnerable Code

The vulnerable application uses user input directly inside the SQL query:

```python
query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
Security Impact

SQL Injection can allow an attacker to manipulate database queries and potentially access or modify data without proper authorization.

Remediation

The secure application uses a parameterized SQL query:

query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))

Parameterized queries separate SQL instructions from user-supplied data and help prevent SQL Injection.

Testing

Both applications were executed successfully.

Vulnerable Application

The application successfully authenticated the test user.

Secure Application

The secure application successfully authenticated the same valid test user using the parameterized query.

Secure Coding Recommendations
Use parameterized queries instead of string concatenation.
Validate and sanitize user input where appropriate.
Avoid exposing sensitive database information.
Use secure password storage such as password hashing in real applications.
Perform regular code reviews and security testing.
Conclusion

The code review identified an SQL Injection vulnerability in the vulnerable application.

The vulnerability was remediated in the secure application by replacing direct SQL string concatenation with a parameterized query.
