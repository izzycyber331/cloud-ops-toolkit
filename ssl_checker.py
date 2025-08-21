import subprocess
import sys

def check_ssl_expiration(hostname):
    """
    Checks the SSL certificate expiration date of a hostname using openssl.
    """
    cmd = f'openssl s_client -connect {hostname}:443 </dev/null 2>/dev/null | openssl x509 -noout -enddate'
    
    try:
        print(f"--- Checking SSL certificate expiration for {hostname} ---")
        output = subprocess.check_output(cmd, shell=True, text=True)
        
        if 'notAfter=' in output:
            expiration_date = output.split('notAfter=')[1].strip()
            print(f"✅ Expiration Date: {expiration_date}")
        else:
            print("❌ Could not retrieve expiration date.")
            
    except subprocess.CalledProcessError as e:
        print(f"Error executing openssl: {e}")
    except FileNotFoundError:
        print("Error: openssl command not found. Please ensure it is installed.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ssl_checker.py <hostname>")
        sys.exit(1)
    
    hostname_to_check = sys.argv[1]
    check_ssl_expiration(hostname_to_check)
