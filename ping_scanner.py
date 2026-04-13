import subprocess      # To run system commands like ping
import platform        # To detect OS (Windows/Linux/Mac)
import re              # To extract data using regex


def ping_host(host):
    """
    Function to ping a given host and display results
    """
    try:
        # Detect OS type
        os_type = platform.system().lower()

        # Set parameter based on OS
        # Windows uses -n, Linux/Mac uses -c
        param = '-n' if os_type == 'windows' else '-c'

        # Run ping command
        result = subprocess.run(
            ['ping', param, '4', host],   # Ping 4 times
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=10                   # Timeout after 10 seconds
        )

        output = result.stdout

        # Check if ping was successful
        if result.returncode == 0:
            print(f"\nHost: {host}")
            print("Status: Reachable")

            # Extract average time using regex
            if os_type == 'windows':
                match = re.search(r'Average = (\d+)ms', output)
            else:
                match = re.search(r'avg.*?= .*?/(\d+\.\d+)/', output)

            avg_time = match.group(1) if match else "Not Found"

            print(f"Average Response Time: {avg_time} ms")

        else:
            print(f"\nHost: {host}")
            print("Status: Unreachable")

    except subprocess.TimeoutExpired:
        print("Request timed out!")

    except Exception as e:
        print("Error occurred:", e)


# Main execution block
if __name__ == "__main__":
    print("Ping Scanner")

    # Ask user if multiple hosts
    choice = input("Ping multiple hosts? (y/n): ")

    if choice.lower() == 'y':
        hosts = input("Enter hosts separated by comma: ").split(',')

        for host in hosts:
            ping_host(host.strip())   # Remove extra spaces

    else:
        host = input("Enter hostname or IP: ")
        ping_host(host)