# Network Scanning Automation

## Project Description

This project automates essential network scanning tools using Python.

It includes three main programs:

* **Ping Scanner** – Checks whether a host is reachable and calculates response time  
* **ARP Scanner** – Retrieves and displays IP-MAC address mappings from the ARP table  
* **Nmap Scanner** – Performs network scanning such as host discovery, port scanning, and service detection  

This project demonstrates the use of Python for cybersecurity and network reconnaissance tasks.


## Requirements

* Python 3.6 or higher  
* Nmap installed on the system  


## How to Install Nmap

1. Download Nmap from:  
   https://nmap.org/download.html  

2. Install using default settings  

3. Make sure:
   * Add Nmap to PATH is selected  
   * Npcap is installed  

### Verify Installation

nmap -v


## How to Run Each Program

Open terminal in VS Code and run:

### Ping Scanner

python ping_scanner.py

### ARP Scanner

python arp_scanner.py

### Nmap Scanner

python nmap_scanner.py


## Example Usage

### Ping Scanner

**Single Host**

Ping multiple hosts? n  
Enter hostname or IP: google.com  

**Multiple Hosts**

Ping multiple hosts? y  
Enter hosts: google.com, 8.8.8.8, 127.0.0.1  


### ARP Scanner

python arp_scanner.py  
Save results to file? y  


### Nmap Scanner

**Host Discovery**

Enter target IP: 127.0.0.1  
Enter choice: 1  

**Port Scan**

Enter target IP: 127.0.0.1  
Enter choice: 2  


## Project Structure

```
Network-Scanning-Automation/
│
├── Screenshots/
│
├── README.md
├── arp_results.txt
├── arp_scanner.py
├── nmap_results.txt
├── nmap_scanner.py
├── ping_scanner.py
```


## Features

### Ping Scanner

* Supports single and multiple host scanning  
* Extracts response time  
* Cross-platform compatibility  

### ARP Scanner

* Retrieves ARP table  
* Extracts IP-MAC mappings  
* Displays formatted output  
* Option to save results  

### Nmap Scanner

* Checks if Nmap is installed  
* Host discovery scan  
* Port scanning  
* Multiple scan types  
* Option to save results  


## Screenshots

Screenshots are available in the Screenshots/ folder.


## Security & Ethics

* Only scan networks you own or have permission to scan  
* Unauthorized scanning is illegal and unethical  
* This project is for educational purposes only  


## Author

**Darshan S**


## Conclusion

This project automates network scanning tools using Python and provides hands-on experience with real-world cybersecurity techniques.
