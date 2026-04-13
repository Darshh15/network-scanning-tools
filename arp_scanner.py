import subprocess   # To execute arp command
import platform     # To detect OS
import re           # To extract IP-MAC mapping


def get_arp_table():
    """
    Function to retrieve ARP table from system
    """
    try:
        os_type = platform.system().lower()

        # Command differs based on OS
        if os_type == 'windows':
            command = ['arp', '-a']
        else:
            command = ['arp', '-n']

        # Run ARP command
        result = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        return result.stdout

    except Exception as e:
        print("Error:", e)
        return ""


def parse_arp(output):
    """
    Extract IP and MAC addresses using regex
    """
    pattern = r'(\d+\.\d+\.\d+\.\d+)\s+([a-fA-F0-9:-]{17})'
    matches = re.findall(pattern, output)

    return matches


def display(entries):
    """
    Display ARP entries in formatted table
    """
    print("\nIP Address\t\tMAC Address")
    print("-" * 40)

    for ip, mac in entries:
        print(f"{ip}\t\t{mac}")

    print(f"\nTotal entries: {len(entries)}")


def save_to_file(entries):
    """
    Save ARP results to a file
    """
    with open("arp_results.txt", "w") as file:
        for ip, mac in entries:
            file.write(f"{ip} - {mac}\n")


# Main execution
if __name__ == "__main__":
    print("ARP Scanner ")

    print("Scanning ARP table...\n")

    # Get raw ARP output
    output = get_arp_table()

    # Parse IP-MAC mappings
    entries = parse_arp(output)

    # Display results
    display(entries)

    # Ask to save results
    choice = input("Save results to file? (y/n): ")

    if choice.lower() == 'y':
        save_to_file(entries)
        print("Results saved to arp_results.txt")