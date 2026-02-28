# API7 – Server-Side Request Forgery (SSRF)

## 📌 Vulnerability Type
OWASP API7: SSRF

## 🎯 Description
Server fetches arbitrary URL without validation.

## 🧪 Payload

```json
{
  "url": "http://127.0.0.1:5000/debug-info"
}
