import os

servers = ['google.com', 'github.com', '8.8.8.8']

print("--- Pinging servers... ---")

for server in servers:
    response = os.system(f"ping -c 1 {server}")
    if response == 0:
        print(f"✅ {server} is up!")
    else:
        print(f"❌ {server} is down!")


print("test")