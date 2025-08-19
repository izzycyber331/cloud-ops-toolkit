import requests
import sys

def check_https(url):
    """
    Checks if a URL automatically redirects to HTTPS.
    """
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    try:
        # Setting allow_redirects to True (default) will follow the redirect
        response = requests.get(url, allow_redirects=True, timeout=5)
        final_url = response.url

        print(f"--- Checking {url} for HTTPS ---")

        if final_url.startswith('https://'):
            print(f"✅ Success! The website redirects to HTTPS.")
        else:
            print(f"❌ Warning! The website does not redirect to HTTPS.")
        
    except requests.exceptions.RequestException as e:
        print(f"Error checking {url}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python https_checker.py <url>")
        sys.exit(1)
    
    url_to_check = sys.argv[1]
    check_https(url_to_check)
