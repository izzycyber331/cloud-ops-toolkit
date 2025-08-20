import socket
import sys

def scan_ports(host):
    """
    Scans a few common ports on a given host.
    """
    print(f"--- Scanning common ports for {host} ---")
    
    # Common ports to check: HTTP, HTTPS, SSH, FTP, SMTP
    common_ports = [80, 443, 22, 21, 25]
    
    for port in common_ports:
        try:
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set a timeout for the connection attempt
            s.settimeout(1)
            # Attempt to connect to the host and port
            result = s.connect_ex((host, port))
            
            if result == 0:
                print(f"✅ Port {port} is OPEN")
            else:
                print(f"❌ Port {port} is CLOSED")
            
            s.close()
            
        except socket.gaierror:
            print(f"Hostname could not be resolved: {host}")
            sys.exit()
        except socket.error:
            print("Server not responding.")
            sys.exit()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python port_scanner.py <hostname>")
        sys.exit(1)
    
    host_to_scan = sys.argv[1]
    scan_ports(host_to_scan)
