import subprocess   # To run nmap command
import sys          # To exit program


def check_nmap():
    """
    Check if Nmap is installed
    """
    try:
        subprocess.run(
            ['nmap', '-v'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return True
    except FileNotFoundError:
        return False


def run_scan(target, option):
    """
    Run selected Nmap scan
    """
    try:
        # Choose scan type
        if option == '1':
            command = ['nmap', '-sn', target]

        elif option == '2':
            command = ['nmap', target]

        elif option == '3':
            ports = input("Enter port range (e.g., 20-80): ")
            command = ['nmap', '-p', ports, target]

        elif option == '4':
            command = ['nmap', '-sV', target]

        elif option == '5':
            command = ['nmap', '-O', target]

        else:
            print("Invalid option")
            return

        print("\nScanning... Please wait\n")

        # Execute Nmap command
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=60
        )

        print("Scan Results:\n")
        print(result.stdout)

        # Save results
        save = input("Save results to file? (y/n): ")

        if save.lower() == 'y':
            with open("nmap_results.txt", "w") as file:
                file.write(result.stdout)

            print("Results saved to nmap_results.txt")

    except subprocess.TimeoutExpired:
        print("Scan timed out!")

    except Exception as e:
        print("Error:", e)


# Main program
if __name__ == "__main__":
    print("Nmap Scanner")

    # Check if Nmap is installed
    if not check_nmap():
        print("Nmap is NOT installed or not added to PATH.")
        print("Install it or use full path in code.")
        sys.exit()

    print("Nmap is installed ✅")

    # Get user input
    target = input("Enter target IP or network: ")

    print("""
Select Scan Type:
1. Host Discovery (-sn)
2. Port Scan (1-1000)
3. Custom Port Scan
4. Service Version Detection (-sV)
5. OS Detection (-O)
""")

    option = input("Enter choice: ")

    # Run scan
    run_scan(target, option)