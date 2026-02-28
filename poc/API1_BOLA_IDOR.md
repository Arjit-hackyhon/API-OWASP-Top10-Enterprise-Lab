# API1 – Broken Object Level Authorization (BOLA / IDOR)

## 📌 Vulnerability Type
OWASP API1: Broken Object Level Authorization

## 🎯 Description
The API allows access to user data by modifying the object ID in the URL without verifying authorization.

## 🔍 Vulnerable Endpoint
GET /user/<id>

## 🧪 Steps to Reproduce

1. Send request:

GET http://127.0.0.1:5000/user/1

2. Modify ID:

GET http://127.0.0.1:5000/user/2

## ✅ Result
Application returns another user’s data without authentication.

## 📸 Screenshot
Refer: screenshots/01.1_API1_BOLA.png  
Refer: screenshots/01.2_API1_BOLA.png

## 🚨 Impact
Unauthorized data exposure and privacy violation.

## 🛠 Tools Used
- Postman
