📸 Exploitation Evidence (Step-by-Step Proof)

Below are practical demonstrations of all OWASP API Top 10 vulnerabilities exploited in this lab.

Each screenshot contains:

Request method

Endpoint URL

Payload (if applicable)

Response

Status Code

🟢 Server Running

Flask development server running locally on 127.0.0.1:5000.

🔟 OWASP API TOP 10 – Practical Demonstration
1️⃣ API1 – Broken Object Level Authorization (BOLA / IDOR)
Accessing User ID 1

Changing Object ID to Access Another User

✔ Unauthorized access to another user’s data by modifying ID parameter.

2️⃣ API2 – Broken Authentication (SQL Injection)

✔ Authentication bypass using SQL Injection payload:

' OR 1=1 --
3️⃣ API3 – Mass Assignment (Privilege Escalation)
Injecting role=admin

Token Manipulation / Profile Update

Accessing Admin Dashboard

✔ Privilege escalation achieved via mass assignment vulnerability.

4️⃣ API4 – Unrestricted Resource Consumption

✔ No rate limiting or payload restriction → potential DoS condition.

5️⃣ API5 – Broken Function Level Authorization
Attempting Admin Access

Admin Dashboard Access

✔ Function-level access control bypass.

6️⃣ API6 – Business Logic Flaw

✔ Negative transfer manipulation allowed → logical validation failure.

7️⃣ API7 – Server-Side Request Forgery (SSRF)

✔ Internal service accessed through user-controlled URL input.

8️⃣ API8 – Security Misconfiguration

✔ Debug mode enabled
✔ Secret key exposed
✔ Internal configuration leakage

9️⃣ API9 – Improper Inventory Management

✔ Old API version (/api/v1) accessible without restriction.

🔟 API10 – Unsafe Consumption of APIs

Final Result

This lab demonstrates a complete attack chain including:

SQL Injection

IDOR

Privilege Escalation

JWT Abuse

SSRF

Business Logic Exploitation

Misconfiguration Discovery

API Inventory Issues

✔ Blind trust of external API responses → potential injection or data poisoning.
