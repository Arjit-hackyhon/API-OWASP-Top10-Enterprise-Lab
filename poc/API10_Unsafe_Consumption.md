# API10 – Unsafe Consumption of APIs

## 📌 Vulnerability Type
OWASP API10: Unsafe Consumption of APIs

## 🎯 Description
Server trusts external API response blindly.

## 🧪 Payload

```json
{
  "api_url": "https://jsonplaceholder.typicode.com/todos/1"
}

✅ Result

External data processed without validation.

📸 Screenshot

Refer: screenshots/10_API10_Unsafe_API.png

🚨 Impact

Data poisoning or injection risk.
