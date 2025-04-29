import requests
import threading
import time
import random
from datetime import datetime

# === Configuration ===
url = "http://localhost"  # Your site
log_file = "results.log"  # Log file
user_agents = {
    "normal": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "attacker": "curl/7.68.0",
    "bot": "Googlebot/2.1 (+http://www.google.com/bot.html)"
}

# Generate fake IPs
def random_ip():
    return ".".join(str(random.randint(1, 255)) for _ in range(4))

# Write results to log file
def log_result(ip, status_code, user_type):
    with open(log_file, "a") as f:
        f.write(f"[IP: {ip}] [Status: {status_code}] [Time: {datetime.now().strftime('%H:%M:%S')}] [Type: {user_type}]\n")

# Send HTTP request
def send_request(user_type, ip=None):
    ip = ip or random_ip()
    headers = {
        "X-Real-IP": ip,
        "X-Forwarded-For": ip,
        "User-Agent": user_agents[user_type]
    }

    try:
        response = requests.get(url, headers=headers, timeout=3)
        log_result(ip, response.status_code, user_type)
        print(f"{user_type.title()} -> {ip} -> Status: {response.status_code}")
    except Exception:
        log_result(ip, "ERR", user_type)
        print(f"{user_type.title()} -> {ip} -> Error")

# Normal Users
def simulate_normal_users(count=5):
    for _ in range(count):
        send_request("normal")
        time.sleep(2)

# Attackers (low delay, simultaneous)
def simulate_attackers(count=30):
    threads = []
    for _ in range(count):
        t = threading.Thread(target=send_request, args=("attacker",))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

# Bots (multiple requests per bot IP)
def simulate_bots(count=5, burst=10):
    print(f"Simulating {count} bots, each sending {burst} requests quickly.")
    for _ in range(count):
        ip = random_ip()
        for _ in range(burst):
            threading.Thread(target=send_request, args=("bot", ip)).start()
            time.sleep(0.05)  # Super-fast requests

# === Main Demo Flow ===
if __name__ == "__main__":
    print("Starting attack simulation...\n")

    print("🟢 Simulating Normal Users")
    simulate_normal_users()

    print("\n🔴 Simulating Attackers")
    simulate_attackers()

    print("\n🟡 Simulating Bots")
    simulate_bots()

    print("\n✅ Simulation complete! Check results.log and nginx/logs/banned.log")
