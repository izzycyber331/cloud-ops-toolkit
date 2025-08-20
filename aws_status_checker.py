import requests
import sys

def check_aws_status():
    """
    Checks the AWS Health Dashboard for any service issues.
    """
    aws_health_url = "https://health.aws.amazon.com/health/status"
    
    try:
        print("--- Checking AWS Service Health ---")
        response = requests.get(aws_health_url, timeout=10)
        
        if response.status_code == 200:
            status_data = response.json()
            issues_found = False
            
            # The structure of the JSON feed can vary, so this is a simplified check
            if 'service' in status_data:
                for service_info in status_data['service']:
                    if 'status' in service_info and service_info['status'] != 'operational':
                        print(f"❌ Issue found: {service_info['name']} is {service_info['status']}")
                        issues_found = True
            
            if not issues_found:
                print("✅ All AWS services are currently operational.")
            
        else:
            print(f"Error checking AWS status. HTTP Status Code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to AWS Health Dashboard: {e}")
    except ValueError:
        print("Error decoding JSON response.")

if __name__ == "__main__":
    check_aws_status()
