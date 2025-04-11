import requests
import time
import random
import argparse

def run_attack(target_ip, attack_type="normal", duration=600, delay=0.1):
    """
    
    Simulate various traffic patterns against the ESP32
    
    Parameters:
    - target_ip: IP address of the ESP32 (typically 192.168.4.1)
    - attack_type: 
        - "normal": Low request rate, few errors
        - "moderate": Medium request rate, some errors
        - "ddos": High request rate, many errors
        - "gradual": Starts normal, gradually becomes DDoS
    - duration: How long to run the attack in seconds
    - delay: Time between requests (in seconds)
    """
    
    print(f"Starting {attack_type} traffic simulation against {target_ip}")
    print(f"Duration: {duration} seconds")
    print(f"Press Ctrl+C to stop at any time")
    
    base_url = f"http://{target_ip}"
    start_time = time.time()
    request_count = 0
    error_count = 0
    
    try:
        while time.time() - start_time < duration:
            # Determine request parameters based on attack type
            if attack_type == "normal":
                endpoints = ["/"] * 9 + ["/nonexistent"] * 1  # 10% errors
                current_delay = delay
            
            elif attack_type == "moderate":
                endpoints = ["/"] * 7 + ["/test"] * 1 + ["/nonexistent"] * 2  # 20% errors
                current_delay = delay / 2
            
            elif attack_type == "ddos":
                endpoints = ["/"] * 5 + ["/test"] * 2 + ["/nonexistent"] * 3  # 30% errors
                current_delay = delay / 10
            
            elif attack_type == "gradual":
                elapsed = time.time() - start_time
                progress = elapsed / duration
                
                if progress < 0.3:  # First 30% of time - normal
                    endpoints = ["/"] * 9 + ["/nonexistent"] * 1
                    current_delay = delay
                elif progress < 0.6:  # Next 30% - moderate
                    endpoints = ["/"] * 7 + ["/test"] * 1 + ["/nonexistent"] * 2
                    current_delay = delay / 2
                else:  # Final 40% - DDoS
                    endpoints = ["/"] * 5 + ["/test"] * 2 + ["/nonexistent"] * 3
                    current_delay = delay / 10
            
            # Select random endpoint
            endpoint = random.choice(endpoints)
            url = base_url + endpoint
            
            try:
                response = requests.get(url, timeout=1)
                request_count += 1
                
                if response.status_code >= 400:
                    error_count += 1
                    
            except requests.exceptions.RequestException:
                request_count += 1
                error_count += 1
            
            # Print status every 10 requests
            if request_count % 10 == 0:
                elapsed = time.time() - start_time
                rate = request_count / elapsed if elapsed > 0 else 0
                print(f"Requests: {request_count}, Errors: {error_count}, Rate: {rate:.1f} req/sec")
            
            time.sleep(current_delay)
    
    except KeyboardInterrupt:
        print("\nAttack stopped by user")
    
    # Final stats
    elapsed = time.time() - start_time
    print("\n--- Attack Summary ---")
    print(f"Attack type: {attack_type}")
    print(f"Duration: {elapsed:.1f} seconds")
    print(f"Total requests: {request_count}")
    print(f"Total errors: {error_count}")
    print(f"Request rate: {request_count / elapsed:.1f} requests/second")
    print(f"Error rate: {error_count / request_count * 100:.1f}%")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ESP32 Traffic Simulation Tool")
    parser.add_argument("--ip", default="192.168.4.110", help="ESP32 IP address (default: 192.168.4.110)")
    parser.add_argument("--type", default="normal", choices=["normal", "moderate", "ddos", "gradual"], 
                        help="Attack type (default: normal)")
    parser.add_argument("--duration", type=int, default=60, help="Duration in seconds (default: 60)")
    parser.add_argument("--delay", type=float, default=0.1, help="Base delay between requests (default: 0.1)")
    
    args = parser.parse_args()
    
    run_attack(args.ip, args.type, args.duration, args.delay)

