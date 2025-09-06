# Unicode Inline Decoder for Burp Suite

A Burp Suite extension that **automatically decodes `\uXXXX` Unicode escape sequences inline**  
so they are displayed as human-readable characters directly inside Burp (Proxy, Repeater, Intruder, etc.).

---

## ⚡ Difference from [Unicode Decoder Tab](https://github.com/bolbolabadi/unicode-decoder-burp)
- **Unicode Decoder Tab** → adds a separate tab for decoded view (non-intrusive).
- **Unicode Inline Decoder (this project)** → modifies Burp’s requests and responses inline (decoding everywhere directly).

---

## ✨ Features
- Hooks into all Burp HTTP traffic using `IHttpListener`.
- Decodes escaped Unicode (`\u0627\u06cc...`) into readable text (`این`).
- Works with **requests and responses**.
- Useful for testing applications that encode text in Unicode escapes.

---

## ⚠️ Warning
This extension **modifies messages sent to the server** as well as what you see in Burp.  
If you only want to *view decoded text* but keep raw traffic unchanged,  
use [Unicode Decoder Tab](https://github.com/bolbolabadi/unicode-decoder-burp).

---

## 📦 Installation
1. Install **Jython standalone JAR** (Burp → Extender → Options → Python Environment).  
   Download from: https://www.jython.org/download  
2. Clone this repo:
   ```bash
   git clone https://github.com/bolbolabadi/unicode-inline-decoder-burp.git
