# API6 – Business Logic Flaw

## 📌 Vulnerability Type
OWASP API6: Unrestricted Access to Sensitive Business Flows

## 🎯 Description
Negative transfer values allowed.

## 🧪 Payload

```json
{
  "amount": -1000
}
