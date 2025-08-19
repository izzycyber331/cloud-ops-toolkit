import requests
import sys

def check_headers(url):
    """
    Checks for common security headers on a given URL.
    """
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers
        print(f"--- Checking security headers for {url} ---")

        # List of headers to check
        security_headers = {
            'Strict-Transport-Security': "Protects against man-in-the-middle attacks.",
            'X-Frame-Options': "Prevents clickjacking.",
            'Content-Security-Policy': "Prevents code injection attacks.",
            'X-Content-Type-Options': "Prevents MIME-sniffing.",
            'Referrer-Policy': "Controls where referrer information is sent."
        }

        found_count = 0
        missing_count = 0

        for header, description in security_headers.items():
            if header in headers:
                print(f"✅ Found: {header}")
                found_count += 1
            else:
                print(f"❌ Missing: {header}")
                missing_count += 1

        print("\n--- Summary ---")
        print(f"Found {found_count} headers. Missing {missing_count} headers.")

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to {url}: {e}")
        return

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python check_security_headers.py <url>")
        sys.exit(1)
    
    url_to_check = sys.argv[1]
    check_headers(url_to_check)