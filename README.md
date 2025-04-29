# 🛡️ Proxy Server Defender

> 🔐 A Cryptography and Network Security project built to simulate and secure a Django-based web server using NGINX reverse proxy, with advanced request filtering and threat mitigation techniques.

---

## 📌 Project Overview

**Proxy Server Defender** is a backend-focused security system designed to protect web applications by integrating a reverse proxy (NGINX) in front of a Django-based website. The project simulates both normal and malicious users to test the effectiveness of various security mechanisms including:

- 🧱 Reverse Proxy with NGINX
- 🚫 Rate Limiting
- 🤖 Bot Detection and Banning
- 🔍 IP Tracking and Logging
- 📄 Suspicious Request Logging
- 🧪 Traffic Simulation for Testing Defense Logic

This project falls under the **Cryptography and Network Security** domain and demonstrates real-world security techniques for web traffic control and application protection.

---

## 📂 Project Structure

proxy-server-defense/
│
├── 📁 django_site/                # Your Django website project folder
│   ├── manage.py
│   ├── django_site/
│   │   └── settings.py
│   └── ...                        # Usual Django app structure
│
|
│   └── nginx.conf                 # Your NGINX reverse proxy configuration
│
|
│   └── attack.py                  # Python script to simulate traffic (bots + normal users)
│
|
│   └── results.log                # Example log file to store IP tracking, bot detection, etc.


---

## 🛠️ Key Features

- ✅ **Reverse Proxy with NGINX**: Shields the backend Django server from direct exposure.
- 🧠 **Bot Simulation & Detection**: Simulated traffic from bots vs. normal users.
- 📉 **Rate Limiting**: Controls how many requests an IP can make in a given time window.
- 📌 **IP Tracking and Request Logging**: Every request is logged with metadata.
- ❌ **Suspicious Activity Flagging**: Abnormal request patterns are marked and flagged.
- 🔐 **Access Restrictions**: Malicious IPs can be banned or throttled.

---

## 📋 Description of Components

### 🧩 1. `django_site/`
A basic Django project acting as the server-side web application.

### 🧩 2. `nginx/default.conf`
The reverse proxy configuration file where:
- Reverse proxying to Django app is defined.
- Rate limits are set using `limit_req_zone`.
- Suspicious User-Agents or IPs are blocked.
- Access logs are enabled.

### 🧩 3. `simulator/simulate_users.py`
A Python script that simulates various user behaviors:
- Normal users browsing the site.
- Bots sending repeated/frequent requests.
- Custom headers to simulate different agents.

### 🧩 4. `logs/request_logs.txt`
A log file where:
- All request IPs are recorded.
- Suspicious behavior is noted (rate exceeded, bot-like behavior).
- Helps in real-time analysis or later audits.

---

## 🎯 Use Case

This system is ideal for demonstrating:
- Defensive backend infrastructure.
- Simulating real-world traffic scenarios (both benign and malicious).
- Deploying Django apps behind an NGINX layer.
- Learning how to implement effective **rate-limiting**, **logging**, and **IP filtering** using open-source tools.

---

## 📚 Technologies Used

- 🌐 **Django** (Web framework)
- 🌍 **NGINX** (Reverse Proxy & Rate Limiting)
- 🐍 **Python** (Traffic Simulation)
- 📁 **Linux-based Server Configuration** (for deployment/testing)
- 📜 **Log Monitoring** (Custom text-based logging)

---

## 💡 Future Enhancements

- 🔍 Real-time log visualization using dashboards (e.g., Kibana or Grafana)
- ⚙️ Automatic IP ban list updater
- 🧠 ML-based Bot detection module
- 🌐 Web interface for admin to view suspicious logs

---

## 👨‍💻 Author

Made with ❤️ by **Tirth Gajera**

---


