📦 INSTALLATION GUIDE
🔥 API OWASP Top 10 – Enterprise Lab Setup

This guide explains how to install and run the vulnerable API lab step-by-step.

🖥 System Requirements

Windows / Linux / macOS

Python 3.9+

Git (optional)

Postman

🧰 Step 1 – Install Python

Download Python from:

👉 https://python.org

During installation:

✔ Check "Add Python to PATH"

Verify installation:

python --version

Expected output:

Python 3.x.x
📥 Step 2 – Clone Repository (Recommended)

If using Git:

git clone https://github.com/Arjit-hackyhon/API-OWASP-Top10-Enterprise-Lab.git
cd API-OWASP-Top10-Enterprise-Lab

If not using Git:

Download ZIP from GitHub

Extract folder

Open folder in terminal

📦 Step 3 – Install Dependencies

Make sure you are inside project directory.

Run:

pip install -r requirements.txt

Packages installed:

Flask

PyJWT

requests

Verify:

pip list
🗄 Step 4 – Reset Database (Important)

If you previously ran the app, delete:

users.db

This ensures fresh vulnerable database creation.

▶ Step 5 – Run Application

Start the server:

python app.py

Expected output:

Running on http://127.0.0.1:5000

If you see:

Debug mode: on

✔ This is intentional (Security Misconfiguration for lab)

🌐 Step 6 – Verify in Browser

Open:

http://127.0.0.1:5000/debug-info

If JSON appears → server working correctly.

🧪 Step 7 – Install Postman

Download from:

👉 https://www.postman.com/downloads/

Open Postman.

You are now ready to test vulnerabilities.
